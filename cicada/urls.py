from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.index, name='home'),
    path('through_the_borders', views.image),
    path('cipher', views.cipher),
    path('pilots', views.audio),
    path('final', views.final)
]
