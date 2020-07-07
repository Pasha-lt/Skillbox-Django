from .import views
from django.urls import path, include

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list')
]
