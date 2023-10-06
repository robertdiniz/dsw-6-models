from django.db import models

class Disco(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    nome_produtora = models.CharField(max_length=50)
    ano = models.DateField()
    pais = models.CharField(max_length=50)
    GENENEROS_MUSICAIS = [
        ("A", "Eletrônica"),
        ("B", "Rock"),
        ("C", "Phonk"),
        ("D", "jRap"),
    ]
    generos = models.CharField(max_length=30, choices=GENENEROS_MUSICAIS, default="A")
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.nome} - {self.nome_produtora}'

