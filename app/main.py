from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from consultas import df_final

app = FastAPI()

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
    <h3>/get_max_duration/AÑO/PLATAFORMA/TIPO Por ej: /get_max_duration/2020/netflix/min</h3>
    <p>Devuelve la película/serie con mayor duración por plataforma, año y tipo de duración (min o seasons).</p>
    <h3>/get_count_platform/PLATAFORMA Por ej: /get_count_platform/disney</h3>
    <p>Devuelve la cantidad de películas y de series por plataforma</p>
    <h3>/get_listedin/GENERO Por ej: /get_listedin/comedy</h3>
    <p>Devuelve la cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.</p>
    <h3>/get_actor/PLATAFORMA/AÑO Por ej: /get_actor/amazon/2020</h3>
    <p>Devuelve al actor/actriz con mayor número de apariciones según año y plataforma.</p>
    <h3>Luego de realizar alguna consulta, si desea volver a esta guía, elimine los decoradores.</h3>
</body>
</html>"""

@app.get("/get_max_duration/{anio}/{plataforma}/{tipo}")
def get_max_duration(anio,plataforma,tipo):
    anio = int(anio)
    tuple_plataformas = ("amazon","disney","hulu","netflix")
    tuple_tipo = ("min","season")
    if (anio in range(df_final.release_year.min(),df_final.release_year.max()+1)) and (plataforma in (tuple_plataformas)) and (tipo in tuple_tipo):
        id_final = df_final.query(f"release_year == {anio} and platform == '{plataforma}' and duration_type == '{tipo}'").duration_int.idxmax()
        return f'{df_final[id_final:id_final+1].to_dict().get("title").get(id_final)} Tiene la mayor duración: {df_final[id_final:id_final+1].to_dict().get("duration").get(id_final)}'
    else:
        return f"Faltan datos para su consulta o alguno de los parámetros es incorrecto, por favor verifique que los datos ingresados."

@app.get("/get_count_platform/{plataforma}")
def get_count_platform(plataforma):
    tuple_plataformas = ("amazon","disney","hulu","netflix")
    if plataforma in (tuple_plataformas):
        dict = df_final.query(f"platform == '{plataforma}'").groupby(by=['type']).title.count().to_dict()
        return f'El conteo de la plataforma {plataforma} es: {dict.get("Movie")} películas y {dict.get("TV Show")} series'


@app.get("/get_listedin/{genero}")
def get_listedin(genero):
    conteo = df_final[df_final.listed_in.str.contains(genero, case=False)].groupby(by=['platform']).title.count().to_dict()
    return f'El género {genero} aparece {conteo.get("amazon")} veces en amazon, {conteo.get("disney")} veces en disney, {conteo.get("hulu")} veces en hulu y {conteo.get("netflix")} veces en netflix'


@app.get("/get_actor/{plataforma}/{anio}")
async def actores(plataforma,anio):
    anio = int(anio)
    tuple_plataformas = ("amazon","disney","hulu","netflix")
    if (anio in range(df_final.release_year.min(),df_final.release_year.max()+1)) and (plataforma in (tuple_plataformas)):
        actor_list = []
        cast_list = df_final.query(f"platform == '{plataforma}' and release_year == {anio}").cast.tolist()
        for i in range(len(cast_list)):
            actor_list_temp = cast_list[i].split(",")
            for j in range(len(actor_list_temp)):
                if actor_list_temp[j] != 'Sin Datos':
                    actor_list.append(actor_list_temp[j])
        dict_actor = dict(zip(actor_list,map(lambda x: actor_list.count(x),actor_list)))
        max_actor = max(dict_actor, key=dict_actor.get)
        max_actor_appearances = dict_actor.get(max_actor)
        return f'El actor/actriz con mayor número de apariciones en la plataforma {plataforma} el año {anio} es {max_actor} con {max_actor_appearances} apariciones.'
    else:
        return f"Faltan datos para su consulta o alguno de los parámetros es incorrecto, por favor verifique que los datos ingresados."
    