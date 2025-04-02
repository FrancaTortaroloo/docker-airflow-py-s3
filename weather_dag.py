from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.http.sensors.http import HttpSensor
import json
from airflow.providers.http.operators.http import HttpOperator
from airflow.operators.python import PythonOperator
import pandas as pd
import os

#conversion de kelvin a celsius
def kelvin_to_celsius(temp_in_kelvin):
    temp_in_celsius = temp_in_kelvin - 273.15
    return temp_in_celsius

def transform_load_data(task_instance):
    #extraer los datos
    data = task_instance.xcom_pull(task_ids='extract_weather_data')
    
        # Convertir la respuesta JSON a un diccionario (en caso de que sea string)
    if isinstance(data, str):
        data = json.loads(data)
        
    city = data['name']
    weather_description = data['weather'][0]['description']
    temp_celsius = kelvin_to_celsius(data['main']['feels_like'])
    feels_like_celsius = kelvin_to_celsius(data['main']['temp'])
    min_temp_celsius = kelvin_to_celsius(data['main']['temp_min'])
    max_temp_celsius = kelvin_to_celsius(data['main']['temp_max'])
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    time_of_record = datetime.utcfromtimestamp(data['dt'] + data['timezone'])
    sunrise_time = datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset_time = datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])
    
    transformed_data = {"City": city,
                        "Description": weather_description,
                        "Temperature (C)": temp_celsius,
                        "Feels Like (C)": feels_like_celsius,
                        "Minimum Temperature (C)": min_temp_celsius,
                        "Maximum Temperature (C)": max_temp_celsius,
                        "Pressure": pressure,
                        "Humidity": humidity,
                        "Wind Speed": wind_speed,
                        "Time of Record": time_of_record,
                        "Sunrise (Local Time)": sunrise_time,
                        "Sunset (Local Time)": sunset_time
                        }
    #convertir a lista
    transformed_data_list = [transformed_data]
    #convertir a df
    df_data = pd.DataFrame(transformed_data_list)
    #conexion con el bucket s3
    aws_credentials = {"key": "ASIAYOMOIBNAD3A6K7NA",
                       "secret": "wLDSZYPKo32MhxZffToMkeIgqVg9B3XDuO6SgS4M",
                       "token": "FwoGZXIvYXdzEHoaDPRPVLA4qnRi/5QL5SJqZrI/G5INYlJt4YMs3x2Nfy6BV6glKvXdJ/ciYiypxNpMpPOzFAPa1ykvCPXyelilBCKBzLglR9HJDwGcoQcZH72bRT+iwlU4jcv2gjTke4Vx1RJAFnae0KXuYrumzlfggx+Qn/OCtiMxxyiz8LO/BjIouR75n7jp1EIjAg+I0fXdwylqktOQbg1apsTZo1+fuNWLiBzCZs9Dwg=="
                       }
    
    now = datetime.now()
    #extraer fecha y hora
    dt_string = now.strftime("%d%m%Y%H:%M:%S")
    dt_string = 'current_weather_data_malaga_' + dt_string
    #guardar en csv
    df_data.to_csv(f"s3://weather-api-airflow-project/{dt_string}.csv", index=False, storage_options=aws_credentials)


#definir si queremos que nos avise si la api no esta disponible
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    #desde cuando quiero que empiece a trabajar
    'start_date': datetime(2025, 4,1),
    'email':[],
    'email_on_failure': False,
    'email_on_retry': False,
    # si falla la tarea, cuantas veces quiero que lo intente
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}


# cada cuanto quiero que se ejecute
with DAG('weather_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:
    #llamada a la api
        is_weather_api_ready = HttpSensor(
        task_id='is_weather_api_ready',
        http_conn_id='weathermap_api',
        endpoint='/data/2.5/weather?id=2514256&appid=334d12b9e0af8161953fede70b9db206'
    )
        
#extraer data
        extract_weather_data = HttpOperator(
        task_id='extract_weather_data',
        http_conn_id='weathermap_api',
        endpoint='/data/2.5/weather?id=2514256&appid=334d12b9e0af8161953fede70b9db206',
        method='GET',
        response_check=lambda r: json.loads(r.text),
        log_response=True
        )
        
        #transformar data
        #llama la funcion transform_load_data
        transform_load_weather_data = PythonOperator(
        task_id='transform_load_weather_data',
        python_callable=transform_load_data
    )
        
        
        
        
        #conectar las tareas
        is_weather_api_ready >> extract_weather_data >> transform_load_weather_data