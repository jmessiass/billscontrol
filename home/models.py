from django.db import models


class Home(models.Model):
    texto_1 = models.CharField(max_length=50)
    texto_2 = models.CharField(max_length=50)
    imagem = models.ImageField(
        upload_to='home/',
        blank=True,
        null=True,
        help_text='Aceita qualquer imagem sem espaço e caracteres especiais.<br>Tamanho recomendado 400x362.'
    )
    texto_3 = models.CharField(max_length=50)
    ativo = models.BooleanField(default=0)

    def __str__(self):
        return self.texto_1

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'
