# from django.apps import apps
from rest_framework import serializers
from .models import Fonction, Contexte, Dimension, Avancement


# class SearchFilterSerializer(serializers.Serializer):

#     class Meta:
#         app_models = apps.get_app_config('search_filters').get_models()
#         fields = ['name', 'id']


class FonctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fonction
        fields = ['name', 'id']


class ContexteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contexte
        fields = ['name', 'id']


class DimensionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dimension
        fields = ['name', 'id']


class AvancementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avancement
        fields = ['name', 'id']
