from django.contrib import admin
from django.urls import path
from .views import views
from .views.enviar_mensagem_view import EnviarMensagemView


app_name = "broadcasts"

urlpatterns = [
    path('', views.home, name='home'),
    path("enviar-excel/", EnviarMensagemView.as_view(), name="enviar_excel"),
]
