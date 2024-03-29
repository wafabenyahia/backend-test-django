from django.db import models


# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=8)


class Entreprise(models.Model):
    idEntrprise = models.AutoField(primary_key=True)
    raison = models.CharField(max_length=40)
    siret = models.CharField( unique=True, max_length=14)
    adressPostal = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Responsable(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    numTel = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)


class Pdl(models.Model):
    id = models.AutoField(primary_key=True)
    pdl = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=10)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
