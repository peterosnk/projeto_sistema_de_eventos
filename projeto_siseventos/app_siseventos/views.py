import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Evento, Inscricao
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages

#pagina inicial apos login
def home(request):
    if not request.user.is_authenticated:
        return render(request, 'home_publica.html')
    
    eventos = Evento.objects.all()

    eventos_inscritos = Inscricao.objects.filter(
        usuario=request.user
    ).values_list('evento_id', flat=True)

    context = {
        'eventos': eventos,
        'eventos_inscritos': eventos_inscritos,
    }

    return render(request, 'home.html', context)

#cadastro de eventos - apenas para administradores
@staff_member_required
def cadastrar_evento(request):
    if request.method == "GET":
        return render(request, 'cadastrar_evento.html')
    
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')
    data = request.POST.get('data')
    local = request.POST.get('local')

    data_evento = datetime.strptime(data, '%Y-%m-%dT%H:%M')

    Evento.objects.create(
        titulo=titulo,
        descricao=descricao,
        data=data_evento,
        local=local,
        organizador=request.user
    )

    return redirect('app_siseventos:home')

#editar evento - apenas para administradores
@staff_member_required
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == "GET":
        return render(request, 'editar_evento.html', {'evento': evento})

    evento.titulo = request.POST.get('titulo')
    evento.descricao = request.POST.get('descricao')
    data = request.POST.get('data')
    evento.data = datetime.strptime(data, '%Y-%m-%dT%H:%M')
    evento.local = request.POST.get('local')
    evento.save()

    return redirect('app_siseventos:home')

#deletar evento - apenas para administradores
@staff_member_required
def deletar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    evento.delete()
    return redirect('app_siseventos:home')

#inscrição em eventos
@login_required(login_url='app_siseventos:login')
def inscrever_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    
    ja_inscrito = Inscricao.objects.filter(
        usuario=request.user,
        evento=evento
    ).exists()

    if ja_inscrito:
        messages.warning(request, "Você já está inscrito neste evento.")
        return redirect('app_siseventos:home')
    
    Inscricao.objects.create(
        usuario=request.user,
        evento=evento
    )

    messages.success(request, "Inscrição realizada com sucesso!")
    return redirect('app_siseventos:home')

#meus eventos inscritos
@login_required(login_url='app_siseventos:login')
def meus_eventos(request):
    inscricoes = Inscricao.objects.filter(usuario=request.user).select_related('evento')

    return render(request, 'meus_eventos.html', {
        'inscricoes': inscricoes
    })

#cancelar inscrição em eventos
@login_required(login_url='app_siseventos:login')
def cancelar_inscricao(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    
    inscricao = Inscricao.objects.filter(
        usuario=request.user,
        evento=evento
    ).first()

    if not inscricao:
        messages.error(request, "Você não está inscrito neste evento.")
        return redirect('app_siseventos:home')
    
    inscricao.delete()

    messages.info(request, "Inscrição cancelada com sucesso!")
    return redirect('app_siseventos:home')

#tela de cadastro de usuario
def cadastro(request):
    if request.user.is_authenticated:
        return redirect('app_siseventos:home')

    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('senha')
        confirmar_password = request.POST.get('confirmar_senha')

        if password != confirmar_password:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'cadastro.html')

        user = User.objects.filter(username=username).first()

        if user:
            messages.warning(request, "Usuário já existe.")
            return render(request, 'cadastro.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return redirect('app_siseventos:login')

#tela de login
def login(request):
    if request.user.is_authenticated:
        return redirect('app_siseventos:home')

    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('nome')
        password = request.POST.get('senha')

        user = authenticate(username=username, password=password)

        if user is not None:
            login_django(request, user)
            return redirect('app_siseventos:home')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            return render(request, 'login.html')
        
#logout
def logout_view(request):
    logout(request)
    return redirect('app_siseventos:login')

#inscrito em eventos
@staff_member_required
def inscritos_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    inscricoes = Inscricao.objects.filter(evento=evento).select_related('usuario')

    return render(request, 'inscritos_evento.html', {
        'evento': evento,
        'inscricoes': inscricoes
    })

#encerrar evento
@staff_member_required
def encerrar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    evento.ativo = False
    evento.save()
    return redirect('app_siseventos:home')