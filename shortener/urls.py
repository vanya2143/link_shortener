from rest_framework.routers import DefaultRouter

from shortener import views

router = DefaultRouter()
router.register('links', views.LinkViewSet, basename='link')
urlpatterns = router.urls
