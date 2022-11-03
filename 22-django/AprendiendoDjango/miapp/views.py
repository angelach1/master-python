from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (métodos)
#MVT = Modelo Template Vista -> Acciones (métodos)


layout = """
   <h4>Sitio web con Django | Ángel Alhambra</h4>
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
      <li>
         <a href="/contacto-dos">Contacto</a>
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
   return render(request, 'index.html')

def hola_mundo(request):
   return render(request, 'hola_mundo.html')

def pagina(request, redirigir = 0):

   if redirigir == 1:
      return redirect('contacto', nombre = "Ángel", apellidos = "Alhambra")

   return render(request, 'pagina.html')
   
def contacto(request, nombre="", apellidos=""):
   html = ""

   if nombre and apellidos:
      html += "<p>El nombre completo es:</p>"
      html += f"<h3>{nombre} {apellidos}</h3>"
   return HttpResponse(layout + f"<h2>Contacto</h2>" + html)