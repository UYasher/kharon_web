from django.urls import path
from documentation import views

urlpatterns = [
    path('', views.index, name='index')
]