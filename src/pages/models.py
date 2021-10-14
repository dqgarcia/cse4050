from django.db import models
from django.db.models.base import Model


# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=3000)
    image = models.ImageField(upload_to = 'pages', null=True, blank = True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta: 
        verbose_name = "post"
        verbose_name_plural = "posts"