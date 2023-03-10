from django.shortcuts import render,redirect,get_object_or_404
from django.template.context_processors import request

from GrupoArticulosApp.models import Categoria
from .forms import IngresarCategoriaForm
from django.http import HttpResponse

# Create your views here.


def listadoArticulos (request):
    grupoArticulosList = Categoria.objects.values()
    return render(request, 'listadoCategoria.html', {'listado':grupoArticulosList})



def create(request):
    form = IngresarCategoriaForm()
    data = {'forms': form}

    if request.method == 'POST':
        formulario = IngresarCategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']='Datos Guardados'
    return render(request, 'crearCategoria.html', data)




"""
def procesarIngresoCategoria(request):
    form = IngresarCategoriaForm()
    if form.is_valid():
        form.save()
        form = IngresarCategoriaForm()
    return render(request, 'crearCategoria.html', {'forms': form, 'mensaje': 'Categoria Ingresada'})
"""

def buscar(request):

    if request.GET["catBuscar"]:
        #mensaje="Articulo Buscado: %r"%request.GET["catBuscar"]
        categoria=request.GET["catBuscar"]

        resultado=Categoria.objects.filter(descripcion__icontains=categoria)
        return render(request,'listadoCategoria.html',{"categoria":resultado})
    else:
        mensaje="No ah ingresado nada"
    return HttpResponse(mensaje)



def modificarCategoria(request,id):
    categoria = get_object_or_404(Categoria,id=id)

    data = {'forms':IngresarCategoriaForm(instance=categoria)}
    if request.method == 'POST':
        formulario = IngresarCategoriaForm(data=request.POST,instance=categoria)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Datos Guardados'


    return render ( request, 'modificarCategoria.html',data)


def eliminarCategoria(request,id):
    categoria = get_object_or_404(Categoria,id=id)
    categoria.delete()
    return redirect(to='listadoUrl')
