from rest_framework import viewsets

from .serializers import (
    # SearchFilterSerializer,
    FonctionSerializer,
    ContexteSerializer,
    AvancementSerializer,
    DimensionSerializer,)
from .models import Fonction, Contexte, Dimension, Avancement

# Create your views here.


# class SearchFilterViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows cards to be viewed or edited.
#     """
#     queryset = Fonction.objects.all()
#     serializer_class = SearchFilterSerializer


class FonctionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cards to be viewed or edited.
    """
    queryset = Fonction.objects.all()
    serializer_class = FonctionSerializer


class ContexteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cards to be viewed or edited.
    """
    queryset = Contexte.objects.all()
    serializer_class = ContexteSerializer


class DimensionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cards to be viewed or edited.
    """
    queryset = Dimension.objects.all()
    serializer_class = AvancementSerializer


class AvancementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cards to be viewed or edited.
    """
    queryset = Avancement.objects.all()
    serializer_class = DimensionSerializer
