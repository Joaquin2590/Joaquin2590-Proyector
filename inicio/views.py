from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'inicio/home.html')

def acerca(request):
    return render(request, 'inicio/acerca.html')