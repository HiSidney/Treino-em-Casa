from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistroForm
import json
from .models import ProgressoPeso, ProgressoTreino, Marco

# usuarios/views.py ou outro app
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/usuarios/login/')
def painel(request):
    # # Peso
    # pesos_qs = ProgressoPeso.objects.filter(usuario=request.user).order_by("data")
    # pesos = [p.peso for p in pesos_qs]
    # datas = [p.data.strftime("%d/%m") for p in pesos_qs]

    # # Marcos
    # marcos = Marco.objects.filter(usuario=request.user)

    # return render(request, "usuarios/painel.html", {
    #     "pesos": json.dumps(pesos),
    #     "datas": json.dumps(datas),
    #     "marcos": marcos
    # })

        # Simulação de progresso de peso corporal
    pesos = [70, 71, 70.5, 72, 71.8, 72.3]  # em kg
    datas = ["01/08", "08/08", "15/08", "22/08", "29/08", "05/09"]

    # Simulação de repetições/series por semana
    reps = [50, 60, 65, 70, 80, 85]  # total por semana
    semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4", "Semana 5", "Semana 6"]

    # Simulação de marcos
    marcos = [
    {"nome": "Primeira barra fixa", "data": "01/08"},
    {"nome": "10 flexões seguidas", "data": "08/08"},
    {"nome": "Primeiro muscle-up", "data": "15/08"}
]

    return render(request, "usuarios/painel.html", {
        "pesos": json.dumps(pesos),
        "datas": json.dumps(datas),
        "reps": json.dumps(reps),
        "semanas": json.dumps(semanas),
        "marcos": marcos,
    })



def cadastro_view(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # loga após cadastro
            return redirect("/")
    else:
        form = RegistroForm()
    return render(request, "usuarios/cadastro.html", {"form": form})

class LoginCustomView(LoginView):
    template_name = "usuarios/login.html"

class LogoutCustomView(LogoutView):
    template_name = "usuarios/logout.html"