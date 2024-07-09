from django.db import models

class Sl(models.Model):
    nome =  models.CharField(verbose_name='nome',max_length=100, null=False , blank=False)
    senha =  models.CharField(verbose_name='senha',max_length=500, null=False , blank=False)
    criado = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    