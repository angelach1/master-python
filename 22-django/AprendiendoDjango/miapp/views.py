from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (métodos)
#MVT = Modelo Template Vista -> Acciones (métodos)

layout = """
   <h1>Sitio web con Django | Ángel Alhambra</h1>
   </hr>
   <ul>
      <li>
         <a href="/inicio">Inicio</a>
      </li>
      <li>
         <a href="/hola-mundo">Hola Mundo</a>
      </li>
      <li>
         <a href="/pagina-pruebas">Página de pruebas</a>
      </li>
   </ul>
   </hr>
"""

def index(request):
   html = """
      <h1>Esta es la página de Inicio</h1>
      <p>Años pares hasta el 2050:</p>
      <ul>
   """
   year = 2022
   while year <= 2050:
      if year % 2 == 0:
         html += f"<li>{str(year)}</li>"
      year += 1

   html += "</ul>"
   return HttpResponse(layout + html)

def hola_mundo(request):
   return HttpResponse(layout + """
      <h1>Hola mundo con Django!!</h1>
      <h3>Soy Ángel Alhambra WEB</h3>
   """)

def pagina(request):
   return HttpResponse(layout + """
      <h1>Página de mi web</h1>
      <p>Creado por Ángel Alhambra</p>
   """)

def contacto(request, nombre, apellidos):
   return HttpResponse(layout + f"<h2>Contacto {nombre} {apellidos}</h2>")