from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Project

# Create your views here.


class ProjectView(View):

    template_name = "index.html"

    def get(self, request):
        projects = Project.objects.all()

        # return the image url for ajax use
        if projects.exists():
            for project in projects:
                if project.image_url:
                    project.image_url = project.image_url.url

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
            if project.image_url:
                project.image_url = project.image_url.url

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
