from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from consultas import df_final
from consultas import itemgetter

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index():
    return '''<html lang="en">
<head>
<title>PI-01 DTS-05</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-black.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
html,body,h1,h2,h3,h4,h5,h6 {font-family: "Roboto", sans-serif;}
.w3-sidebar {
  z-index: 3;
  width: 250px;
  top: 43px;
  bottom: 0;
  height: inherit;
}
</style>
</head>
<body>

<!-- Navbar -->
<div class="w3-top">
  <div class="w3-bar w3-theme w3-top w3-left-align w3-large">
    <a class="w3-bar-item w3-button w3-right w3-hide-large w3-hover-white w3-large w3-theme-l1" href="javascript:void(0)" onclick="w3_open()"><i class="fa fa-bars"></i></a>
    <a href="#" class="w3-bar-item w3-button w3-theme-l1">Inicio</a>
  </div>
</div>

<!-- Sidebar -->
<nav class="w3-sidebar w3-bar-block w3-collapse w3-large w3-theme-l5 w3-animate-left" id="mySidebar">
  <a href="javascript:void(0)" onclick="w3_close()" class="w3-right w3-xlarge w3-padding-large w3-hover-black w3-hide-large" title="Close Menu">
    <i class="fa fa-remove"></i>
  </a>
  <h4 class="w3-bar-item"><b>Links:</b></h4>
  <a class="w3-bar-item w3-button w3-hover-black" href="https://github.com/Emmafer/PI01_05DATA-ENGINEER" target="_blank">GitHub Repo</a>
  <a class="w3-bar-item w3-button w3-hover-black" href="https://www.youtube.com/watch?v=fEQ04igLrNE" target="_blank">Video Explicativo</a>
</nav>

<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- Main content: shift it to the right by 250 pixels when the sidebar is visible -->
<div class="w3-main" style="margin-left:250px">

  <div class="w3-row w3-padding-64">
    <div class="w3-twothird w3-container">
      <h1 class="w3-text-teal">Guía de Usuario:</h1>
      <h3>Para realizar una consulta, lo único que debe hacer es colocar el decorador correspondiente, indicando los parámetros a utilizar, para realizar una nueva consulta, regrese a ésta página.</h3>
      <h2 class="w3-text-teal">/get_max_duration/{año}/{plataforma}/{tipo}</h2>
      <h5>
      <b><p>Devuelve la película/serie con mayor duración por plataforma, año y tipo de duración (min o seasons).</b> <br><br>Ej: /get_max_duration/2021/hulu/min</p>
      </h5>
    </div>

  <div class="w3-row">
    <div class="w3-twothird w3-container">
      <h2 class="w3-text-teal">/get_count_platform/{plataforma}</h2>
      <h5>
      <b><p>Devuelve la cantidad de películas y de series por plataforma.</b> <br><br>Ej: /get_count_platform/amazon</p>
      </h5>
    </div>

  <div class="w3-row">
    <div class="w3-twothird w3-container">
      <h2 class="w3-text-teal">/get_listedin/{genero}</h2>
      <h5>
      <b><p>Devuelve la cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.</b> <br><br>Ej: /get_listedin/comedy</p>
      </h5>
    </div>

  <div class="w3-row w3-padding-64">
    <div class="w3-twothird w3-container">
      <h2 class="w3-text-teal">/get_actor/{plataforma}/{año}</h2>
      <h5>
      <b><p>Devuelve al actor/actriz con mayor número de apariciones según año y plataforma.</b> <br><br>Ej: /get_actor/netflix/2020</p>
      </h5>
    </div>
  </div>
  
<!-- END MAIN -->
</div>

<script>
// Get the Sidebar
var mySidebar = document.getElementById("mySidebar");

// Get the DIV with overlay effect
var overlayBg = document.getElementById("myOverlay");

// Toggle between showing and hiding the sidebar, and add overlay effect
function w3_open() {
  if (mySidebar.style.display === 'block') {
    mySidebar.style.display = 'none';
    overlayBg.style.display = "none";
  } else {
    mySidebar.style.display = 'block';
    overlayBg.style.display = "block";
  }
}

// Close the sidebar with the close button
function w3_close() {
  mySidebar.style.display = "none";
  overlayBg.style.display = "none";
}
</script>

</body>
</html>
'''

@app.get("/get_max_duration/{anio}/{plataforma}/{tipo}")
async def get_max_duration(anio,plataforma,tipo):
    anio = int(anio)
    tuple_plataformas = ("amazon","disney","hulu","netflix")
    tuple_tipo = ("min","season")
    try:
        if (anio in range(df_final.release_year.min(),df_final.release_year.max()+1)) and (plataforma in (tuple_plataformas)) and (tipo in tuple_tipo):
            id_final = df_final.query(f"release_year == {anio} and platform == '{plataforma}' and duration_type == '{tipo}'").duration_int.idxmax()
            return f'{df_final[id_final:id_final+1].to_dict().get("title").get(id_final)} Tiene la mayor duración: {df_final[id_final:id_final+1].to_dict().get("duration").get(id_final)}'
        else:
            return f"Faltan datos para su consulta o alguno de los parámetros es incorrecto, por favor verifique que los datos ingresados."
    except ValueError:
            return f"La plataforma {plataforma} no posee registros en {anio}"

@app.get("/get_count_platform/{plataforma}")
async def get_count_platform(plataforma):
    tuple_plataformas = ("amazon","disney","hulu","netflix")
    if plataforma in (tuple_plataformas):
        dict = df_final.query(f"platform == '{plataforma}'").groupby(by=['type']).title.count().to_dict()
        return f'El conteo de la plataforma {plataforma} es: {dict.get("Movie")} películas y {dict.get("TV Show")} series'
    else:
        return f"Faltan datos para su consulta o alguno de los parámetros es incorrecto, por favor verifique que los datos ingresados."

@app.get("/get_listedin/{genero}")
async def get_listedin(genero):
    try:
        dict_plat = df_final[df_final.listed_in.str.contains(genero, case=False)].groupby(by=['platform']).title.count().to_dict()
        max_value = max(dict_plat.items(), key=itemgetter(1))[0]
        return f'la plataforma {max_value} tiene la mayor frecuencia de género {genero}, apareciendo {dict_plat.get(max_value)} veces'
    except ValueError:
        return f'No hay registros de {genero} en ninguna de nuestras plataformas.'

@app.get("/get_actor/{plataforma}/{anio}")
async def get_actor(plataforma, anio):
    anio = int(anio)
    tuple_plataformas = ("amazon","disney","hulu","netflix")
    try:
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
    except ValueError:
        return f"La plataforma indicada no posee registros en {anio}"