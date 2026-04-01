"""
Módulo de modelo da model usuário.
"""
from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser # type: ignore


class Usuario(AbstractUser):
    """ classe para representar o entidade usuário. """
    
    email = models.EmailField(
        unique=True,
        verbose_name= "E-mail",
    )

    rg = models.CharField(
        max_length=11,
        unique=True,
        blank=True,
        null=True,
        verbose_name="RG",
    )

    cpf = models.CharField(
        max_length=11,
        unique=True,
        blank=True,
        null=True,
        verbose_name="CPF",
    )

    data_nascimento = models.DateField(
        blank=True,
        null=True,
        verbose_name="Data de Nascimento",
    )
    
    celular = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Celular",
    )

    telefone = models.CharField(
        max_length=12,
        blank=True,
        null=True,
        verbose_name="Telefone Fixo",
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em",
    )

    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em",
    )

    class Meta:
        """ 
        Metaclasse para o modelo usuário. 
        """
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        db_table = "usuarios_usuario"
        ordering = ("id",)

    def __str__(self) -> str:
        return f"{self.first_name}"
    