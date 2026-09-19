from django.db import models

class Documento(models.Model):
    titulo = models.CharField(max_length=100)
    # O arquivo será salvo diretamente dentro de MEDIA_ROOT (.arquivos)
    arquivo = models.FileField(upload_to='') 
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
