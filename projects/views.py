from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters

from .serializers import ProjectSerializer
from .models import Project

# Create your views here.


class ProjectFilter(FilterSet):
    # set a filterset to use filters
    # you can use: http://django-filter.readthedocs.io/en/latest/guide/rest_framework.html#using-the-filter-fields-shortcut
    # but it won't let you use "exclude"
    insensitive_name = filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Project
        exclude = ['image', 'lien_pdf']
        fields = '__all__'


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cards to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filter_class = ProjectFilter
    ordering_fields = '__all__'  # what field can be ordered via the API
    ordering = ['pk']  # default ordering


class ProjectView(View):

    template_name = "index.html"

    def get(self, request):
        projects = Project.objects.all()

        # return the image url for ajax use
        if projects.exists():
            for project in projects:
                if project.image:
                    project.image = project.image.url

        projects_json = serializers.serialize("json", projects)

        context = {
            "projects": projects_json,
        }

        # if the request is an ajax request, we return a JsonResponse
        if request.is_ajax():
            return JsonResponse(context)

        # else, we return the render of the template
        else:
            return render(request, self.template_name, context)


class ProjectViewDetail(View):

    template_name = "index.html"

    def get(self, request, id):

        project = Project.objects.get(pk=id)

        if project:
            if project.image:
                project.image = project.image.url

        project_json = serializers.serialize("json", [project])

        context = {
            "project": project_json,
        }

        # if the request is an ajax request, we return a JsonResponse
        if request.is_ajax():
            return JsonResponse(context)

        # else, we return the render of the template
        else:
            return render(request, self.template_name, context)
