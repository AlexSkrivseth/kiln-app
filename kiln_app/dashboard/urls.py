from django.urls import path
from dashboard import views


urlpatterns = [
    path('old_dash', views.main),
    path('dev', views.dev),
    path('kiln/<int:kiln_id>/', views.kiln),
    path('main_dev', views.main_dev),
    path('', views.main_dev),
    path('joke', views.joke),


]
