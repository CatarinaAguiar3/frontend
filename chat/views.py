from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

@login_required(login_url="login")
def index(request):
    return render(
        request,
        "chat/index.html",
        {
            "backend_chat_url": settings.BACKEND_CHAT_URL,
        },
    )

def login(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, "chat/login.html")

def logout(request):
    auth_logout(request)
    messages.success(request, "Você saiu com sucesso.")
    return redirect("login")    