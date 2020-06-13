from django.urls import path, re_path
from django.views.generic import TemplateView, RedirectView

from . import views

urlpatterns = [
    path('', views.post_productos, name='post_productos'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('producto/nuevo/<str:codigo>', views.producto_nuevo, name='producto_nuevo'),
    path('producto/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('producto/<int:pk>/borrar/', views.borrar_producto, name='borrar_producto'),
    path('producto/codigo_de_barras/<str:codigo>', views.editar_producto_con_codigo_de_barras,
         name='editar_producto_codigo_de_barras'),
    path('scanner', TemplateView.as_view(template_name='LibroDiario/scanner.html'), name='scanner'),
]
