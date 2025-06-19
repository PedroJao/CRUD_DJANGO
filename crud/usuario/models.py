from django.db import models

# Create your models here.
class Usuario(models.Model):
    uid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contato = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'usuario'