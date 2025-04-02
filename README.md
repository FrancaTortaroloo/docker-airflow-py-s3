# Weather api

In this project, together with [Nahuel Nuñez Rojas](https://github.com/nahuel-nunez-rojas), we have developed an ETL project.

Technologies used:

📍 Docker\
📍 Apache Airflow\
📍 OpenWeather API\
📍 Python in VS Code\
📍 Amazon S3

## First step: Creating the Docker container

We created a Docker container with the Ubuntu operating system and required 2 cores to work with Airflow.

![Imagen de Docker](https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/Images/Container%20Docker.png)

## Second step: Setting up the Python environment and installing Airflow on Ubuntu

We created a Python environment and installed Airflow on Ubuntu.

![Imagen Airflow en Docker](https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/Images/Airflow%20en%20Docker.png)

## Third step: Writing the ETL code in Python

VS Code was connected to the Ubuntu container in Docker. The ETL code can be found in the .py file in the repository: [weather_dag.py]((https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/weather_dag.py))

## Fourth step: Extracting the OpenWeather API credentials

This allows us to make API calls and extract weather data from the city of Málaga, including weather description, temperature, thermal sensation, maximum and minimum temperature, atmospheric pressure, humidity, wind speed, date, sunrise time, and sunset time.

![Imagen OpenWeather](https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/Images/OpenWeather.png)

## Fifth step: Orchestrating the ETL process in Apache Airflow

![Imagen ETL en Airflow](https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/Images/ETL%20en%20airflow.png) 

## Sixth step: Creating an S3 bucket

An S3 bucket was created, along with credentials, to enable saving the CSV file in the bucket from Python.

![Imagen bucket S3](https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/Images/Bucket%20s3.png)

------

En este proyecto en conjunto con [Nahuel Nuñez Rojas](https://github.com/nahuel-nunez-rojas), hemos hecho un proyecto de ETL.

Tecnologías usadas:

📍 Docker\
📍 Apache Airflow\
📍 API de OpenWeather\
📍 Python en VS Code \
📍 Amazon S3 

## Primer paso: Creación del container en Docker

Hemos creado un container en Docker donde tiene el sistema operativo de Ubuntu y necesitábamos 2 núcleos para trabajar con Airflow.

![Imagen de Docker](https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/Images/Container%20Docker.png)

## Segundo paso: Creación del enviroment de Python e instalación de Airflow en Ubuntu

Creamos un enviroment de Python e instalamos Airflow en Ubuntu. 

![Imagen Airflow en Docker](https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/Images/Airflow%20en%20Docker.png)

## Tercer paso: Escribir el código de ETL en Python
Se hizo la conexción de VS Code al contenedor de Ubuntu en Docker. El código del ETL se puede ver en el archivo .py que se encuentra en el repositorio(https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/weather_dag.py)

## Cuarto paso: Extraer las credenciales de la API de OpenWeather

Y así poder hacer las llamadas a la API, donde se extrae la descripción del tiempo de la ciudad de Málaga, temperatura, sensación térmica, temperatura máxima, mínima, presión atmosférica, humedad, velocidad del viento, fecha, horario del amanecer, horario de la puesta de sol.

![Imagen OpenWeather](https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/Images/OpenWeather.png)

## Quinto paso: Orquestación del ETL en Apache Airflow

![Imagen ETL en Airflow](https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/Images/ETL%20en%20airflow.png) 

## Sexto paso: Creación de bucket S3

Se creó un bucket S3, se crearon credenciales para habilitar que desde Python se guarde el archivo de CSV en el bucket.

![Imagen bucket S3](https://github.com/FrancaTortaroloo/docker-airflow-py-s3/blob/main/Images/Bucket%20s3.png)




