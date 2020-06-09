import django_filters
from LibroDiario.models import Producto


class FiltroProductos(django_filters.FilterSet):
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre', 'descripcion', ]
