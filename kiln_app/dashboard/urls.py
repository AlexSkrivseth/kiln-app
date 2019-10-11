from django.urls import path
from dashboard import views


urlpatterns = [
    path('', views.index),
    path('kiln/<int:kiln_id>/', views.kiln),


]
