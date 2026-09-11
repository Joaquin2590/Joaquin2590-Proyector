from django.shortcuts import render

# Create your views here.
def perfil(request):
    return render(request, 'perfil/perfil.html')

def contacto(request):
    return render(request, 'perfil/contacto.html')