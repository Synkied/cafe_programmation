from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Function(models.Model):
    name = models.CharField(max_length=256)


class Context(models.Model):
    name = models.CharField(max_length=256)


class Dimension(models.Model):
    name = models.CharField(max_length=256)


class Advancement(models.Model):
    name = models.CharField(max_length=256)


class Project(models.Model):
    title = models.CharField(_("title"), max_length=256)
    sponsor = models.CharField(_("sponsor"), max_length=128)
    mission = models.TextField(_("mission"))
    architect = models.CharField(_("architect"), max_length=128)
    description = models.TextField(_("description"), max_length=512)
    external_link = models.URLField(_("external_link"), blank=True, null=True)
    pdf_link = models.FileField(_("pdf_link"), blank=True, null=True)
    image = models.ImageField(_("image"), blank=True, null=True)
    function = models.ForeignKey(Function, on_delete=models.CASCADE)
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    advancement = models.ForeignKey(Advancement, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
