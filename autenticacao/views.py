import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
from django.core.exceptions import ValidationError

from usuarios.models import Usuario

log = logging.getLogger(__name__)


def login_user(request):
    if request.user.is_authenticated:
        request.session['email'] = request.user.email
        return redirect('/dashboard/')
    
    if request.method != 'POST':
        return render(request, 'autenticacao/login.html')
    
    username = request.POST['username']
    password = request.POST['password']
    remember = request.POST.get('remember', None) == 'true'
    
    # Válida se o e-mail e a senha foram preenchidos
    if not username or not password:
        messages.error(request, 'É necessário informar o e-mail e a senha.')
        return redirect('/')
    
    # Autentica o usuário
    user = authenticate(request, username=username, password=password)
    
    # Válida se o usuário foi autenticado
    if user is not None:
        if user.is_active:
            login(request, user)
            if remember:
                request.session.set_expiry(5184000)
            return redirect('dashboard/', {'email': user.email})
        messages.error(request, 'Este usuário está inativo.')
        return redirect('/')
    messages.error(request, 'E-mail ou Senha incorretos.')
    return redirect('/')
    
def logout_user(request):
    """
    Realiza o logout do usuário e redireciona para a página inicial com uma mensagem de sucesso.

    Args:
        request (HttpRequest): O objeto de solicitação HTTP.

    Returns:
        HttpResponse: Redireciona para a página inicial com a mensagem de sucesso.
    """
    logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect("/")
