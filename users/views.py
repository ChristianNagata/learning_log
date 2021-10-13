from django.shortcuts import redirect, render
from learning_log.settings import LOGOUT_REDIRECT_URL
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    return render(request, 'registration/login.html')


def logout_view():
    return LOGOUT_REDIRECT_URL


def register(request):
    """Faz o cadastro de um novo usuário."""
    if request.method != 'POST':
        # Exibe o formulário de cadastro em branco
        form = UserCreationForm()
    else:
        # Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Faz login do usuário e o redireciona para a página inicial
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect('index')

    context = {'form': form}
    return render(request, 'register.html', context)
