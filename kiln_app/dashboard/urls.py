from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.index),
    path('kiln/<int:kiln_id>/', views.kiln),
    path('kiln/<int:kiln_id>/change-load/', views.change_load),
    path('kiln/<int:kiln_id>/create-report', views.create_report)

]
