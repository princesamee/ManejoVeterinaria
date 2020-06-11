from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from LibroDiario.filters import FiltroProductos
from LibroDiario.forms import FormularioProducto
from .models import Producto


def post_productos(request):
    productos = Producto.objects.all().order_by('nombre')
    filtro_productos = FiltroProductos(request.GET, queryset=productos)
    return render(request, 'LibroDiario/post_productos.html', {'filter': filtro_productos})


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'LibroDiario/detalle_producto.html', {'producto': producto})


def producto_nuevo(request):
    if request.method == "POST":
        form = FormularioProducto(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.fecha_creacion = timezone.now()
            producto.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = FormularioProducto()

    return render(request, 'LibroDiario/editar_producto.html', {'form': form})


def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = FormularioProducto(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.published_date = timezone.now()
            producto.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = FormularioProducto(instance=producto)
    return render(request, 'LibroDiario/editar_producto.html', {'form': form})
