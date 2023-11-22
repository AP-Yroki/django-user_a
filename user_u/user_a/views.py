from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requsest, f, i, o, age, interests):
    return HttpResponse(f'''
     <h2> О пользователе</h2>
    <p>Фамилия: {f}</p>
    <p>Имя: {i}</p>
    <p>Отчество: {o}</p>
    <p>Возраст: {age}</p>
    <p>Интересы: {interests}</p>''')

def about(request, place, progress, learning):
    return HttpResponse(f'''
    <p>Откуда приехал: {place}</p>
    <p>Успеваемость в школе: {progress}</p>
    <p>Любите / не любите учиться: {learning}</p>''')


def contacts(request):
    return HttpResponse('<p>Мой github: <a href="https://github.com/AP-Yroki">https://github.com/AP-Yroki</a></p>')