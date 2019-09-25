from django.urls import path
from dashboard import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('kiln/<int:kiln_id>/', views.kiln),


]
