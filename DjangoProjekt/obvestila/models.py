from django.db import models
from datetime import date

class Trener(models.Model):
    uporabnisko_ime = models.CharField(max_length=20)
    geslo = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    slika = models.ImageField(default='/static/obvestila/img/contact.png')

    def __str__(self):
        return self.uporabnisko_ime

class Obvestilo(models.Model):
    besedilo = models.CharField(max_length=500)
    avtor = models.ForeignKey(Trener, on_delete=models.CASCADE)
    datum = models.DateField()

    def __str__(self):
        return self.besedilo

class Stars(models.Model):
    email = models.EmailField(max_length=50)

    def __str__(self):
        return  self.email

