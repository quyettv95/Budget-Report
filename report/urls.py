from django.urls import path, register_converter
from . import views

urlpatterns = [
  path('download-sample', views.downloadSample, name='download-sample'),
  path('', views.sample, name='upload'),
]
