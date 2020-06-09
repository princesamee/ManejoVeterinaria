from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_productos, name='post_productos'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('producto/nuevo/', views.producto_nuevo, name='producto_nuevo'),
    path('producto/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
]
