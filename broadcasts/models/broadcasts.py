"""
Módulo de modelo da model atendimento.
"""
from django.db import models # type: ignore


class Broadcasts(models.Model):
    """ Classe para representar a entidade broadcast. """

    STATUS_ENVIO_CHOICES = (
        ('Enviado com sucesso', 'Enviado com sucesso'),
        ('Erro ao enviar', 'Erro ao enviar'),
    )

    id = models.AutoField(
        primary_key=True,
        verbose_name="Id",
    )
    
    nome = models.CharField(
        max_length=20,
        verbose_name="Nome",
    )

    numero_destinatario = models.CharField(
        max_length=20,
        verbose_name="Numero Destinatário",
    )

    status_envio = models.CharField(
        max_length=50,
        choices=STATUS_ENVIO_CHOICES,
        default=None,
        verbose_name='Status',
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em",
    )

    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em",
    )

    objects = models.Manager()

    class Meta:
        """
        Metaclasse para o modelo broadcast.
        """
        verbose_name = "Broadcast"
        verbose_name_plural = "Broadcasts"
        db_table = "broadcasts_broadcast"
        ordering = ("id",)

    def __str__(self) -> str:
        return f"{self.nome} - {self.numero_destinatario}"
    