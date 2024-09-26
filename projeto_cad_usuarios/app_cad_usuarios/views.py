from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

#def usuarios(request):
    #salvar os dados da tela para o banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibir todos os usuarios ja cadastrados em uma nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #retornar os dados para a pagina de listagem de usuarios
    return render(request,'usuarios/usuarios.html',usuarios)

def usuarios(request):
    if request.method == 'POST':
        # Somente salva se o formulário foi enviado via POST
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')

        # Verifica se idade é um número e se nome não está vazio
        if novo_usuario.nome and novo_usuario.idade.isdigit():
            novo_usuario.save()

    # Exibe todos os usuários cadastrados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retorna os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)