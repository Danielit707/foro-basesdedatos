# app/models.py
from django.db import models
from django.conf import settings

class TipoPost(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    tipo = models.ForeignKey(TipoPost, on_delete=models.SET_NULL, null=True, related_name='posts')
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    def __str__(self):
        return f'Comentario {self.id} - {self.autor}'
