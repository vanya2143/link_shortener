from django.urls import path

from shortener import views

urlpatterns = [
    path('', views.LinkList.as_view(), name='link-list'),
    path('export/', views.ExportView.as_view(), name='link-export'),
    path('links/<hash>/', views.LinkDetail.as_view(), name='link-detail'),
]
