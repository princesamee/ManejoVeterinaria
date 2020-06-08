from django.shortcuts import render

from .models import Producto

def post_productos(request):
    productos = Producto.objects.all()
    return render(request, 'LibroDiario/post_productos.html', {'productos': productos})