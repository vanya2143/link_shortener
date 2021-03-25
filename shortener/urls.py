from django.urls import path

from shortener import views


urlpatterns = [
    path('', views.LinkList.as_view(), name='link-list'),
    path('links/<hash>/', views.LinkDetail.as_view(), name='link-detail'),
]

