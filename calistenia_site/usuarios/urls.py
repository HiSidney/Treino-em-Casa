from django.urls import path
from . import views # traz todas as funções do arquivo views
# . = tudo

urlpatterns = [
    path('painel/', views.painel, name='painel'),  # página inicial do usuário
    path("cadastro/", views.cadastro_view, name="cadastro"),
    path("login/", views.LoginCustomView.as_view(), name="login"),
    path("logout/", views.LogoutCustomView.as_view(), name="logout"),
    path("progresso/", views.progresso_view, name="progresso"),
    path("registrar-peso/", views.registrar_peso, name="registrar_peso"),
    path("registrar_progresso/", views.registrar_progresso, name='registrar_progresso'),

]