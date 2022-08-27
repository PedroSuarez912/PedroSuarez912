from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola soy django")

def xd(request):
    ac= "0 "
    x = 0
    y = 1
    for i in range(10):
        x = y + x
        y = x + y
        ac += (str(x)+" "+str(y)+" ")
    return HttpResponse(ac)

def probando_template(request):
    vars = {
        'nombre' : 'peter',
        'edad' : '18',
        'momento' : datetime.now()
    }
    #render tiene 3 parametros 1 opcional
    # render(request(si o si), nombre archivohtml(si o si), contexto)
    return render(request,'template1.html',vars)