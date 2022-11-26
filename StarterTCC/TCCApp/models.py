from django.db import models
from uuid import uuid4
# Create your models here.

def upload_image_mockup(instance, filename):
    return f"{instance.id_mockup}-{filename}"

class Users(models.Model):
    usuario = models.CharField(max_length=16)
    senha = models.CharField(max_length=16)
    email = models.CharField(max_length=256)

class Upload(models.Model):
    id_upload = models.IntegerField(primary_key=True, default=uuid4, editable=False)
    img = models.ImageField(upload_to=upload_image_mockup, blank=False, null=False)
    usuario = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="Mockup_Usuario")
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome