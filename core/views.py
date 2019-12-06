from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello World</h1>')

def soma(request, n1, n2):
    n3 = n1 + n2
    return HttpResponse('<h1>A soma de {} mais {} é igual a {}</h1>'.format(n1,n2,n3))

def subtrai(request, n1, n2):
    n3 = n1 - n2
    return HttpResponse('<h1>A subtração de {} menos {} é igual a {}</h1>'.format(n1,n2,n3))

def multiplica(request, n1, n2):
    n3 = n1 * n2
    return HttpResponse('<h1>A multiplicação de {} vezes {} é igual a {}</h1>'.format(n1, n2, n3))

def divide(request, n1, n2):
    n3 = n1 / n2
    return HttpResponse('<h1>A divisão de {} por {} é igual a {}</h1>'.format(n1, n2, n3))

