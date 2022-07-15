from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# MVC - Modelo Vista Controlador -> Acciones (metodos)
# MVT -  Modelo Vista Template -> Acciones (metodos)

layout = """
    <h1>Bienvenido a la página de inicio</h1>
    <hr>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/hola-django">Hola Django</a>
        </li>
        <li>
            <a href="/pagina-pruebas">Página de pruebas</a>
        </li>
        <li>
            <a href="/contacto">Contacto</a>
        </li>
    </ul>
    <hr> 


"""



def index(request):
    html = """
        <br><br>
        <h3>Años hasta el 2050</h3>
        <ul>
    """

    year = 2022
    while year <= 2060:

        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
    
        year += 1

    html += "</ul>"

    return HttpResponse(layout+html)


def hola_django(request):
    return HttpResponse(layout+
    """
        <center>
        <h1>Universidad Tecnólogica de Tehuacán</h1>
        <h2>Django - Python - Web</h2>
        <h3>DDI - 9A</h3>
        </center>
    """)

def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect('contacto', nombre="Víctor", apellidos="Alvarez")

    return HttpResponse(layout+
        """
            <h1>Página Web</h1>
            <h3>Materia DDI - Python - Django - Web</h3>
        """
    )

def contacto(request, nombre="", apellidos=""):
    html= ""

    if nombre and apellidos:
        html += "<p>El nombre completo es:</p>"
        html += f"<h3>{nombre} {apellidos}</h3>"
    return HttpResponse(layout+f"<h2>Contacto {nombre} {apellidos}</h2>"+html)