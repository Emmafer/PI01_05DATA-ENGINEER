# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

## Introducción:

¡Hola! Mi nombre es Emmanuel Fernandez, al momento de hacer este proyecto me encuentro cursando la etapa de Labs para la carrera de Data Science de SoyHenry. Este proyecto busca situarnos en el rol de un Data Engineer.

## Objetivo: 

Realizar un trabajo de ETL sobre los datasets recibidos, luego, levantar una API con esos datos limpios a la que se le puedan realizar diferentes consultas.

Las consultas a realizar son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:
    El request debe ser: get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma
    El request debe ser: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
    El request debe ser: get_listedin('genero')  
    Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

+ Actor que más se repite según plataforma y año.
    El request debe ser: get_actor(plataforma, año)

Plus: Realizar un deployment de la API en una plataforma "code to cloud" como por ejemplo, Mogenius.

## Explicación de los contenidos del Repositorio:

+ En la carpeta `app` se encuentran los datasets analizados además del `main.py` que es el archivo en el cual se configura FastAPI y se instancian los decoradores de la API.

+ En el notebook `ETL.ipynb` se encuentra el código comentado paso por paso, explicando las decisiones tomadas a la hora de encarar este proyecto de ETL;
    Esto se hizo así para tener dividido de manera ordenada los bloques de código, separados por los markdowns que van separando las etapas del proceso.
    Con esto espero documentar y demostrar cada paso del desarrollo

+ En el archivo `consultas.py` se encuentra el mismo código del notebook `ETL.ipynb` pero más optimizado y sin comentarios.
    De esta forma puedo tener mi código de una manera más resumida y de fácil acceso para importar en mi `main.py` las funciones declaradas.

+ En el archivo `Dockerfile` se encuentra el entorno containerizado de Docker con FastAPI.

## Herramientas utilizadas:

+ Python.

+ Pandas.

+ Docker.

+ FastAPI.

+ HTML.