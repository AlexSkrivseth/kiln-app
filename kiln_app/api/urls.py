from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

router.register('readings', views.ReadingModelViewSet, base_name='readings')

urlpatterns = []

urlpatterns += router.urls
