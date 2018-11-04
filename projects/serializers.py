from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    fonction = serializers.ReadOnlyField(
        source="fonction.name",
        read_only=True,
    )
    contexte = serializers.ReadOnlyField(
        source="contexte.name",
        read_only=True,
    )
    dimension = serializers.ReadOnlyField(
        source="dimension.name",
        read_only=True,
    )
    avancement = serializers.ReadOnlyField(
        source="avancement.name",
        read_only=True,
    )

    class Meta:
        model = Project
        fields = '__all__'
