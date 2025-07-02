from django.contrib import admin
from django.urls import path
from usuario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.NovoUsuario, name='novo_usuario'),
    path('ver_usuarios/', views.VerUsuarios, name='ver_usuarios'),
    path('editar_usuario/<int:uid>/', views.EditarUsuario, name='editar_usuario'),
    path('atualizar_usuario/<int:uid>/', views.AtualizarUsuario, name='atualizar_usuario'),
    path('deletar_usuario/<int:uid>/', views.DeletarUsuario, name='deletar_usuario'),
]
