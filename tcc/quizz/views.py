from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, 'inicio.html')

def quizz(request):
    return render(request, 'form.html')

def create(request):
    req = request
    nome = req.GET['name']
    email = req.GET['email']
    try:
        usuario = Usuario(nome=nome, email=email, score=0)
        usuario.save()

        return render(request, 'questions.html')
    except ValueError as e:
        raise ValueError(e)
