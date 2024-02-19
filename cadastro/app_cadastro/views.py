from django.shortcuts import render
from .models import usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.id_usuario = request.POST.get('id_usuario')
        novo_usuario.save()
    
    usuarios_dic = {
        'usuarios': usuario.objects.all()
    }
    
    return render(request, 'usuarios/usuarios.html', usuarios_dic)
