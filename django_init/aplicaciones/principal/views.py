from django.shortcuts import render,redirect
from .models import Productos
from .forms import ProductosForm
from rest_framework import viewsets
from .serializers import ProductosSerializer



def inicio(request):
    productos = Productos.objects.all()
    cxt = {
        'productos':productos
    }
    return render(request,'index.html', cxt)

def agregarProducto(request):
    
    if request.method == 'GET':

        form = ProductosForm()
        cxt = {
            'form':form
        }
    else:
        form=ProductosForm(request.POST)
        print(form)
        cxt = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'agregar-producto.html', cxt)




def editarProducto(request, codigo):
    producto = Productos.objects.get(codigo = codigo)
    if request.method == 'GET':
        form = ProductosForm(instance = producto)
        cxt = {
            'form' : form
        }
    else:
        form = ProductosForm(request.POST, instance= producto)
        cxt ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'agregar-producto.html', cxt)

def eliminarProducto(request, codigo):
    producto = Productos.objects.get(codigo = codigo)
    producto.delete()
    return redirect('index')


    #API#
class ProductosViewSet(viewsets.ModelViewSet):
    serializer_class = ProductosSerializer
    queryset=Productos.objects.all()