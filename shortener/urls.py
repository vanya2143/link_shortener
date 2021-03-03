from django.urls import path

from shortener.views import LinkList, LinkRedirectView, ExportView


urlpatterns = [
    path('', LinkList.as_view(), name='link-list'),
    path('export/', ExportView.as_view(), name='link-export'),
    path('<url_hash>/', LinkRedirectView.as_view(), name='link-detail'),
]
