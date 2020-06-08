from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_productos, name='post_productos'),
]