from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, 'main/main.html')
    
def trendingnow(request):
    return render(request, 'main/trendingnow.html')

def c1(request):
    return render(request, 'main/c1.html')

def c2(request):
    return render(request, 'main/c2.html')

def c3(request):
    return render(request, 'main/c3.html')