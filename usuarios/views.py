from django.shortcuts import render


app_name = "usuarios"

def home(request):
    return render(request, "usuarios/usuarios.html")