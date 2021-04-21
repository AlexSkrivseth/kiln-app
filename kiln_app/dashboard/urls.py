from django.urls import path
from dashboard import views


urlpatterns = [
    path('', views.main),
    path('dev', views.dev),
    path('kiln/<int:kiln_id>/', views.kiln),
    path('main_dev', views.main_dev),


]
