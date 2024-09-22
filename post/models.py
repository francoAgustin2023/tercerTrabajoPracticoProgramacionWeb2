from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posteos_hechos')
    
    def __str__(self):
        return f"Usuario: {self.autor} - Titulo: {self.titulo} - Contenido: {self.contenido}"