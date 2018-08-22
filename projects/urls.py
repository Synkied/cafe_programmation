from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = "projects"

urlpatterns = [
    path('', (views.ProjectView.as_view()), name="project_list"),
    path('<int:id>', (views.ProjectViewDetail.as_view()), name="project_detail"),
]
