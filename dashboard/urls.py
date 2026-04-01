from django.contrib import admin
from django.urls import path
from .import views


app_name = "dashboard"

urlpatterns = [
    path('', views.home, name='home'),
    path("dados-broadcasts/", views.dados_broadcasts, name="dados_broadcasts"),
    path("baixar-excel-tabela-broadcast/", views.baixar_excel_tabela_broadcast, name="baixar_excel_tabela_broadcast"),
    path("baixar-excel-tabela-broadcast/<str:data_inicial>/<str:data_final>/", views.baixar_excel_tabela_broadcast, name="baixar_excel_tabela_broadcast"),
]
