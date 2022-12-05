from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from consultas import get_max_duration,get_count_platform,get_listedin,get_actor

app = FastAPI()

import pandas as pd

@app.get("/",response_class=HTMLResponse)
async def index():
    return """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proyecto Individual N°1 - Data Engineering</title>
</head>
<body>
    <h1>Guía de Usuario de la API</h1>
    <h3>/get_max_duration-AÑO-PLATAFORMA</h3>
    <p>Devuelve un diccionario que contiene la máxima duración según tipo de film por plataforma y año.</p>
    <h3>/get_count_platform-PLATAFORMA</h3>
    <p>Devuelve un diccionario que contiene la cantidad de películas y de series por plataforma</p>
    <h3>/get_listedin-GENERO</h3>
    <p>Devuelve un diccionario que contiene la cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.</p>
    <h3>/get_actor-PLATAFORMA-AÑO</h3>
    <p>Devuelve un diccionario que contiene el actor que más se repite según plataforma y año.</p>
</body>
</html>"""

@app.get("/get_max_duration-")
async def index():
    return {"get_max_duration":"get_max_duration()"}