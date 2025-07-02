from django.shortcuts import render, redirect, get_object_or_404
from usuario.models import Usuario
from usuario.forms import UsuarioForm

def NovoUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'home.html', {'form': form})

def VerUsuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'ver_usuarios.html', {'usuarios': usuarios})

def EditarUsuario(request, uid):
    usuario = get_object_or_404(Usuario, uid=uid)
    form = UsuarioForm(instance=usuario)
    return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})

def AtualizarUsuario(request, uid):
    usuario = get_object_or_404(Usuario, uid=uid)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('ver_usuarios')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})

def DeletarUsuario(request, uid):
    usuario = get_object_or_404(Usuario, uid=uid)
    usuario.delete()
    return redirect('ver_usuarios')
