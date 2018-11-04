from rest_framework import routers
from projects import views as project_views
from search_filters import views as search_views


router = routers.DefaultRouter()
router.register(r'projects', project_views.ProjectViewSet, base_name="project")
router.register(r'fonctions', search_views.FonctionViewSet, base_name="fonction")
router.register(r'contextes', search_views.ContexteViewSet, base_name="contexte")
router.register(r'dimensions', search_views.DimensionViewSet, base_name="dimension")
router.register(r'avancements', search_views.AvancementViewSet, base_name="avancement")
# router.register(r'search_filters', search_views.SearchFilterViewSet, base_name="search_filter")
