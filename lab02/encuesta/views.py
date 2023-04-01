from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/formulario.html',context)

def calculadora(request):
    context = {
        'titulo': "Calculadora",
    }
    return render(request, 'calculadora/formulario.html',context)

def cilindro(request):
    context = {
        'titulo': "Calculo del Volumen de un cilindro",
    }
    return render(request, 'cilindro/formulario.html',context)





def enviarcilindro(request):
    d = float(request.POST['diametro']) / 2
    a = float(request.POST['altura'])
    r = 3.1416 * pow(d,2) * a 
    context = {
        'titulo':"Calculo",
        'd': d,
        'r': r,
    }
    return render(request,'cilindro/respuesta.html',context,{'r': r})

def enviarcalculadora(request):
    
    context = {
        'titulo':"Respuesta",
        'num1': request.POST['num1'],
        'num2' : request.POST['num2'],
        'operacion' : request.POST['operacion'],
        
    }
    return render(request,'calculadora/respuesta.html',context)

def enviar(request):
    
    context = {
        'titulo':"Respuesta",
        'nombre': request.POST['nombre'],
        'clave' : request.POST['password'],
        'educacion' : request.POST['educacion'],
        'nacionalidad' : request.POST['nacionalidad'],
        'idiomas' : request.POST.getlist('idiomas'),
        'correo' : request.POST['email'],
        'website' : request.POST['sitioweb'],
    }
    return render(request,'encuesta/respuesta.html',context)
