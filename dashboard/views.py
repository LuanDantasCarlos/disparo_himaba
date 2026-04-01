from typing import Optional
from datetime import datetime, timedelta

from openpyxl import Workbook

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from broadcasts.models import Broadcasts


app_name = "dashboard"

@login_required
def home(request):
    context = {
    }

    return render(request, "dashboard/dashboard.html", context)

def dados_broadcasts(request):
    try:
        broadcasts_formatados = [
            {   'id': atendimento['id'],
                'nome': atendimento['nome'] or '-',
                'numero_destinatario': atendimento['numero_destinatario'] or '-',
                'status_envio': atendimento['status_envio'] or '-',
                'criado_em': atendimento['criado_em'] or '-',
            }
            for atendimento in Broadcasts.objects.all().values(
                'id', 'nome', 'numero_destinatario', 'status_envio', 'criado_em'
            ).order_by("-id")
        ]

        return JsonResponse(list(broadcasts_formatados), safe=False)
    except Exception as exc:
        return JsonResponse({"status": 500, "message": str(exc)}, status=500)

def baixar_excel_tabela_broadcast(request, data_inicial: Optional[str] = None, data_final: Optional[str] = None) -> JsonResponse:
    all_broadcasts = Broadcasts.objects.all()
    data_final_ajustada = None

    if data_final != "none":
        data_final_ajustada = datetime.strptime(data_final, "%Y-%m-%d") + timedelta(days=1)
        data_final_ajustada = data_final_ajustada.strftime("%Y-%m-%d")

    # Verifica se as datas foram passadas e ajusta o filtro conforme a situação
    if data_inicial != "none" and data_final != "none":
        # Filtra entre data_inicial e data_final
        filtered_atendimentos = all_broadcasts.filter(criado_em__range=[data_inicial, data_final_ajustada])
    elif data_inicial != "none":
        # Filtra a partir de data_inicial até o final
        filtered_atendimentos = all_broadcasts.filter(criado_em__gte=data_inicial)
    elif data_final != "none":
        # Filtra desde o início até data_final
        filtered_atendimentos = all_broadcasts.filter(criado_em__lte=data_final_ajustada)
    else:
        # Se nenhuma data foi passada, usa todos os registros
        filtered_atendimentos = all_broadcasts

        # Ordena e seleciona os campos desejados
    atendimentos_filtered = filtered_atendimentos.order_by("-id").values(
        "id",
        "nome",
        "numero_destinatario",
        "status_envio",
        "criado_em",
    )

    # Criando o arquivo Excel
    wb = Workbook()
    ws = wb.active
    ws.title = "Broadcasts"

        # Cabeçalhos
    colunas = [
        "Id",
        "Nome",
        "Número do Destinatário",
        "Status da Mensagem",
        "Horário do Envio",
    ]

    ws.append(colunas)

    # Adicionando dados
    for atendimentos_item in atendimentos_filtered:
        ws.append(
            [
                atendimentos_item["id"] if atendimentos_item["id"] else "-",
                atendimentos_item["nome"] if atendimentos_item["nome"] else "-",
                atendimentos_item["numero_destinatario"] if atendimentos_item["numero_destinatario"] else "-",
                atendimentos_item["status_envio"] if atendimentos_item["status_envio"] else "-",
                atendimentos_item["criado_em"] if atendimentos_item["criado_em"] else "-",
            ]
        )

    # Criar uma resposta HTTP com o arquivo Excel
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = "attachment; filename=broadcasts.xlsx"

    # Salvar o arquivo Excel na resposta HTTP
    wb.save(response)
    return response
