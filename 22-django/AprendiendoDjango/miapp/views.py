from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (métodos)
# MVT = Modelo Template Vista -> Acciones (métodos)


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
   """
   html = ""
      <h1>Esta es la página de Inicio</h1>
      <p>Años pares hasta el 2050:</p>
      <ul>
   ""
   year = 2022
   while year <= 2050:
      if year % 2 == 0:
         html += f"<li>{str(year)}</li>"
      year += 1

   html += "</ul>"
   """
   year = 2022
   hasta = range(year, 2051)

   nombre = "Ángel Alhambra"

   lenguajes = ["JavaScript", "Python", "PHP", "C"]
   
   return render(request, 'index.html', {
      'title': 'Inicio',
      'mi_variable': 'Soy un dato que está en la vista',
      'nombre': nombre,
      'lenguajes': lenguajes,
      'years': hasta
   })

def hola_mundo(request):
   return render(request, 'hola_mundo.html')

def pagina(request, redirigir = 0):

   if redirigir == 1:
      return redirect('contacto', nombre = "Ángel", apellidos = "Alhambra")

   return render(request, 'pagina.html', {
      'texto': "Este es mi texto",
      'lista': ["uno", "dos", "tres", "cuatro", "cinco"]
   })
   
def contacto(request, nombre="", apellidos=""):
   html = ""

   if nombre and apellidos:
      html += "<p>El nombre completo es:</p>"
      html += f"<h3>{nombre} {apellidos}</h3>"
   return HttpResponse(layout + f"<h2>Contacto</h2>" + html)

def crear_articulo(request, title, content, public):
   articulo = Article(
      title = title,
      content = content,
      public = public
   )

   articulo.save()

   return HttpResponse(f"Artículo creado: <strong>{articulo.title}</strong> - {articulo.content}")

def articulo(request):
   try:
      articulo = Article.objects.get(title = "Superman", public = False)
      response = f"<h1>Artículo: <br/> {articulo.id} - {articulo.title}</h1>"
   except:
      response = "<h1>Artículo no encontrado</h1>"

   return HttpResponse(response)

def editar_articulo(request, id):
   articulo = Article.objects.get(pk = id)
   
   articulo.title = "Batman"
   articulo.content = "Película del 2017"
   articulo.public = True
   
   articulo.save()

   return HttpResponse(f"Artículo {articulo.id} editado: <strong>{articulo.title}</strong> - {articulo.content}")

def articulos(request):
   #articulos = Article.objects.order_by('id')[2:4]
   articulos = Article.objects.all()
   #articulos = Article.objects.filter(title = "Batman")
   #articulos = Article.objects.filter(title__contains = "artículo")
   #articulos = Article.objects.filter(id__lte = 7, title__contains = "artículo")
   #articulos = Article.objects.filter(id__gte = 7, title__contains = "artículo")
   
   #articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE id = 5")

   #uso de OR con Django
   #Usar import Q 
   articulos = Article.objects.filter(
      Q(title__contains = "Cuarto") | Q(title__contains = "Batman")
   )

   return render(request, 'articulos.html', {
      'articulos': articulos
      }
   )

def borrar_articulo(request, id):
   articulo = Article.objects.get(pk = id)

   articulo.delete()

   return redirect('articulos')
