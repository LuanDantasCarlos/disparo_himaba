""" Módulo para possibilitar autenticação de usuário por e-mail ou username """
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class UsernameOrEmailBackend(ModelBackend):
    """Classe responsável por autenticar usuário por username ou e-mail """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """ Método que autentica o usuário por username ou e-mail """
        user_model = get_user_model()

        # Verifica se o username é um e-mail
        if '@' in username:
            try:
                user = user_model.objects.get(email=username)
            except user_model.DoesNotExist:
                return None
        else:
            try:
                user = user_model.objects.get(username=username)
            except user_model.DoesNotExist:
                return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
