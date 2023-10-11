from django.db import models

class Selo(models.Model):
    nome_produtora = models.CharField(max_length=50)
    def __str__(self):
        return self.nome_produtora

class Artista(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Disco(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=250)
    selo = models.ForeignKey(Selo, on_delete=models.CASCADE, blank=True, null=True)
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
    artistas = models.ManyToManyField(Artista, related_name="discos")

    def __str__(self):
        return f'{self.nome} - {self.selo}'

