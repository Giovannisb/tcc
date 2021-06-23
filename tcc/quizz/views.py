from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'inicio.html')

def quizz(request):
    return render(request, 'form.html')

def create(request):
    req = request
    x = 2