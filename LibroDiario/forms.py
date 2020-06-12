from django import forms

from .models import Producto


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'categoria', 'codigo_de_barras')
