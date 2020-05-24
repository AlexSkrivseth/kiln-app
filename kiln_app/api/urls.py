from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()


router.register(r'readings', views.ReadingModelViewSet, base_name='readings')
router.register(r'loads', views.LoadModelViewSet, base_name='loads')

urlpatterns = []

urlpatterns += router.urls
