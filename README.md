# Weather api

En este proyecto en conjunto con [Nahuel Nuñez Rojas](https://github.com/nahuel-nunez-rojas), hemos hecho un proyecto de ETL.

Tecnologías usadas:

📍 Docker\
📍 Apache Airflow\
📍 API de OpenWeather\
📍 Python en VS Code \
📍 Amazon S3 

## Primer paso: Creación del container en Docker

Hemos creado un container en Docker donde tiene el sistema operativo de Ubuntu y necesitábamos 2 núcleos para trabajar con Airflow.

![Imagen de Docker](https://github.com/FrancaTortaroloo/docker-airflow-py-s3/tree/main/Images)

## Segundo paso: Creación del enviroment de Python e instalación de Airflow en Ubuntu

Creamos un enviroment de Python e instalamos Airflow en Ubuntu. 

![Imagen Airflow en Docker](https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/Images/Airflow%20en%20Docker.png)

## Tercer paso: Escribir el código de ETL en Python

Esto se puede ver en el archivo .py que se encuentra en el repositorio(https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/weather_dag.py)

## Cuarto paso: Extraer las credenciales de la API de OpenWeather

Y así poder hacer las llamadas a la API, donde se extrae la descripción del tiempo de la ciudad de Málaga, temperatura, sensación térmica, temperatura máxima, mínima, presión atmosférica, humedad, velocidad del viento, fecha, horario del amanecer, horario de la puesta de sol.

![Imagen OpenWeather](https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/Images/OpenWeather.png)

## Quinto paso: Orquestación del ETL en Apache Airflow

![Imagen ETL en Airflow](https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/Images/ETL%20en%20airflow.png) 

## Sexto paso: Creación de bucket S3

Se creó un bucket S3, se crearon credenciales para habilitar que desde Python se guarde el archivo de CSV en el bucket.

![Imagen bucket S3](https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/Images/Bucket%20s3.png)




