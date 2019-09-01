from django.db import models
from django.utils.translation import gettext_lazy as _

from search_filters.models import Fonction
from search_filters.models import Contexte
from search_filters.models import Dimension
from search_filters.models import Avancement
# Create your models here.


class Project(models.Model):
    titre = models.CharField(_("titre"), max_length=256)
    commanditaire = models.CharField(_("commanditaire"), max_length=256)
    mission = models.TextField(_("mission"))
    concepteur = models.CharField(_("concepteur"), max_length=256)
    description = models.TextField(_("description"), max_length=362)
    explicatif = models.TextField(
        _("explicatif"),
        max_length=362,
        blank=True,
        null=True
    )
    lien_externe = models.URLField(_("lien externe"), blank=True, null=True)
    lien_pdf = models.FileField(_("lien pdf"), blank=True, null=True)
    image = models.ImageField(_("image"), blank=True, null=True)
    fonction = models.ForeignKey(
        Fonction,
        null=True,
        on_delete=models.SET_NULL
    )
    contexte = models.ForeignKey(
        Contexte,
        null=True,
        on_delete=models.SET_NULL
    )
    dimension = models.ForeignKey(
        Dimension,
        null=True,
        on_delete=models.SET_NULL
    )
    avancement = models.ForeignKey(
        Avancement,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
