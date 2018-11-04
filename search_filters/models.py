from django.db import models

# Create your models here.


class Fonction(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Contexte(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Dimension(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Avancement(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
