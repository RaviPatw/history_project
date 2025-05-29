from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('unit/<str:unit_id>/',views.unit_page,name='unit_page'),
    path('themes',views.themes,name="themes")
]
