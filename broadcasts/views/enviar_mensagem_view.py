from django.views import View
from django.http import JsonResponse
import pandas as pd
from time import sleep
import logging
from whatsapp.services import WhatsappService
from broadcasts.models import Broadcasts

whatsapp_service = WhatsappService()

log = logging.getLogger(__name__)

class EnviarMensagemView(View):
    def post(self, request):
        """
        Recebe um arquivo Excel e uma mensagem enviados via AJAX (FormData).
        Lê os dados do Excel e retorna uma resposta JSON.
        """
        # Pega o arquivo e a mensagem do request
        arquivo_excel = request.FILES.get("arquivo_excel")
        mensagem = request.POST.get("mensagem")

        # Valida se os campos foram enviados
        if not arquivo_excel or not mensagem:
            return JsonResponse(
                {"erro": "Envie um arquivo Excel e uma mensagem."},
                status=400
            )

        try:
            numeros = self.extrai_numeros_excel(arquivo_excel)

            for numero in numeros:
                try:
                    result = whatsapp_service.send_message(
                        destinatario=numero,
                        message=mensagem
                    )

                    log.info(result)
                    print()
                    Broadcasts.objects.create(
                        nome = "",
                        numero_destinatario=numero,
                        status_envio="Enviado com sucesso",
                    ), sleep(3)
                except Exception as exc:
                    Broadcasts.objects.create(
                        nome = "",
                        numero_destinatario=numero,
                        status_envio="Erro ao enviar",
                    )
            # Retorna sucesso
            return JsonResponse(
                {
                    "mensagem": "Excel processado.",
                    "total_contatos": len(numeros)
                },
                status=200
            )

        except Exception as exc:
            return JsonResponse(
                {"erro": f"Erro ao processar o arquivo Excel: {str(exc)}"},
                status=500
            )
        
    def extrai_numeros_excel(self, arquivo_excel):
        # Lê o Excel usando pandas
        df = pd.read_excel(arquivo_excel)

        # Verifica se a coluna 'numero' existe
        if "numero" not in df.columns:
            return JsonResponse(
                {"erro": "O arquivo Excel deve conter uma coluna chamada 'numero'."},
                status=400
            )

        # Converte os números para string (para evitar erros com números grandes)
        numeros = df["numero"].astype(str).tolist()

        # Remove espaços e linhas vazias
        numeros = [n.strip() for n in numeros if n.strip()]

        return numeros
