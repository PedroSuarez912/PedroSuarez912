from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import datetime

from .models import Familiar
# Create your views here.


def templateFlia(request):
    familiar1 = Familiar(
        nombre="Laura",
        edad=43,
        altura = 1.58,
        matrimonio = False,
        nacimiento = datetime.date(1979,6,1)
    )
    familiar2 = Familiar(
        nombre="Felipe",
        edad=13,
        altura=1.62,
        matrimonio = False,
        nacimiento = datetime.date(2009,5,14)
    )
    familiar3 = Familiar(
        nombre="lucia",
        edad=22,
        altura=1.58,
        matrimonio = False,
        nacimiento = datetime.date(2000,2,22)
    )
    dicc = {
        "uno" : familiar1,
        "dos" : familiar2,
        "tres" : familiar3
    }
    
    familiar1.save()
    familiar2.save()
    familiar3.save()

    return render(request,'familia.html',dicc)