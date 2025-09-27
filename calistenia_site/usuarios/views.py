from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistroForm
import json
from .models import PesoCorporal, Treino, Marco, PlanoAlimentar, Alimento, Cronograma
from .forms import PesoCorporalForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/usuarios/login/')
def painel(request):
    # Busca todos os registros de peso do usuário logado
    pesos_db = PesoCorporal.objects.filter(usuario=request.user).order_by("data")

    # Separa em listas para o gráfico
    pesos = [p.peso for p in pesos_db]
    datas = [p.data.strftime("%d/%m") for p in pesos_db]  # formato dd/mm

    # (por enquanto ainda simulamos reps e marcos, até criarmos os models deles)
    reps = [50, 60, 65, 70, 80, 85]
    semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4", "Semana 5", "Semana 6"]
    marcos = ["Primeira barra fixa", "10 flexões seguidas", "Primeiro muscle-up"]

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
            return redirect("usuarios/painel/")
    else:
        form = RegistroForm()
    return render(request, "usuarios/cadastro.html", {"form": form})

class LoginCustomView(LoginView):
    template_name = "usuarios/login.html"

class LogoutCustomView(LogoutView):
    template_name = "usuarios/logout.html"



@login_required(login_url='/usuarios/login/')
def progresso_view(request):
    return render(request, "usuarios/progresso.html")


@login_required(login_url='/usuarios/login/')
def registrar_peso(request):
    if request.method == "POST":
        form = PesoCorporalForm(request.POST)
        if form.is_valid():
            peso_obj = form.save(commit=False)  # ainda não salva no banco
            peso_obj.usuario = request.user     # vincula ao usuário logado
            peso_obj.save()                     # agora sim salva
            return redirect("painel")           # volta para o painel do usuário
    else:
        form = PesoCorporalForm()

    return render(request, "usuarios/registrar_peso.html", {"form": form})

@login_required(login_url='/usuarios/login/')
def registrar_progresso(request):
    return render(request, "usuarios/registrar_progresso.html")