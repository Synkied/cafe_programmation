from django.db import models
from django.utils.translation import gettext_lazy as _
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


class Project(models.Model):
    titre = models.CharField(_("titre"), max_length=256)
    commanditaire = models.CharField(_("commanditaire"), max_length=128)
    mission = models.TextField(_("mission"))
    concepteur = models.CharField(_("concepteur"), max_length=128)
    description = models.TextField(_("description"), max_length=362)
    lien_externe = models.URLField(_("lien externe"), blank=True, null=True)
    lien_pdf = models.FileField(_("lien pdf"), blank=True, null=True)
    image = models.ImageField(_("image"), blank=True, null=True)
    fonction = models.ForeignKey(Fonction, on_delete=models.CASCADE)
    contexte = models.ForeignKey(Contexte, on_delete=models.CASCADE)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    avancement = models.ForeignKey(Avancement, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
