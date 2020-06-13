from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from LibroDiario.filters import FiltroProductos
from LibroDiario.forms import FormularioProducto
from .models import Producto


def post_productos(request):
    productos = Producto.objects.filter(habilitado=True).order_by('nombre')
    filtro_productos = FiltroProductos(request.GET, queryset=productos)
    return render(request, 'LibroDiario/post_productos.html', {'filter': filtro_productos})


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'LibroDiario/detalle_producto.html', {'producto': producto})


def producto_nuevo(request, codigo):
    if request.method == "POST":
        form = FormularioProducto(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.fecha_creacion = timezone.now()
            producto.fecha_ultima_modificacion = timezone.now()
            producto.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        default_data = {'codigo_de_barras': codigo}
        form = FormularioProducto(default_data)
    return render(request, 'LibroDiario/editar_producto.html', {'form': form})


def editar_producto_con_codigo_de_barras(request, codigo):
    producto = Producto.objects.filter(codigo_de_barras=codigo)
    if len(producto) == 0:
        return redirect('producto_nuevo', codigo=codigo)
    else:
        return redirect('editar_producto', pk=producto[0].pk)


def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = FormularioProducto(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.habilitado = True
            producto.fecha_ultima_modificacion = timezone.now()
            producto.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = FormularioProducto(instance=producto)
    return render(request, 'LibroDiario/editar_producto.html', {'form': form})


def borrar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.habilitado = False
        producto.fecha_ultima_modificacion = timezone.now()
        producto.save()
        return redirect('post_productos')
    return render(request, 'LibroDiario/borrar_producto.html', {'producto': producto})
