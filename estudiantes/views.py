from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumnx, Primer_parcial
from .forms import AlumnxForm, Primer_parcialForm, Segundo_parcialForm, FinalForm, AutobiografiaForm
from django.contrib import messages
from django.db.models.functions import Coalesce
from decimal import Decimal


def lista_alumnx(request):
    alumnxs = Alumnx.objects.order_by('nombre')
    return render(request, 'estudiantes/lista_alumnx.html', {'alumnxs':alumnxs})

def alumnx_nuevo(request):
    if request.method == "POST":
        form_alumnx = AlumnxForm(request.POST)
        if form_alumnx.is_valid():
            alumnx = form_alumnx.save()
            alumnx.save()
            return redirect('lista_alumnx')
    else:
        form_alumnx = AlumnxForm()
    return render(request, 'estudiantes/alumnx_edit.html', {'form_alumnx':form_alumnx})

def alumnx_edit(request, pk):
    alumnx = get_object_or_404(Alumnx, pk=pk)
    if request.method == "POST":
        form_alumnx = AlumnxForm(request.POST, instance=alumnx)
        if form_alumnx.is_valid():
            alumnx = form_alumnx.save()
            alumnx.save()
            return redirect('lista_alumnx')
    else:
        form_alumnx = AlumnxForm(instance=alumnx)
    return render(request, 'estudiantes/alumnx_edit.html', {'form_alumnx': form_alumnx})

def eliminar_alumnx(request, pk):
    try:
        alumnx = Alumnx.objects.get(pk=pk)
    except Alumnx.DoesNotExist:
        messages.error(request, "Alumnx que quieres eliminar no existe")
        return redirect('lista_alumnx')
    alumnx.delete()
    messages.error(request, f"Alumnx ha sido eliminado")
    return redirect('lista_alumnx')

def lista_calif1erpar(request):
    primer_parcials = Primer_parcial.objects.order_by('nombre')
    return render(request, 'estudiantes/lista_calif1erpar.html', {'primer_parcials':primer_parcials})

def primer_parcial(request):
    if request.method == "POST":
        form_1erparcial = Primer_parcialForm(request.POST)
        if form_1erparcial.is_valid():
            primer_parcial = form_1erparcial.save()
            primer_parcial.save()
            return redirect('lista_calif1erpar')
    else:
        form_1erparcial = Primer_parcialForm()
    return render(request, 'estudiantes/calificacion_1erparcial_edit.html', {'form_1erparcial':form_1erparcial})

def primer_parcial_edit(request, pk):
    primer_parcial = get_object_or_404(Primer_parcial, pk=pk)
    if request.method == "POST":
        form_1erparcial = Primer_parcialForm(request.POST, instance=primer_parcial)
        if form_1erparcial.is_valid():
            primer_parcial = form_1erparcial.save()
            primer_parcial.save()
            return redirect('lista_calif1erpar')
    else:
        form_1erparcial = Primer_parcialForm(instance=primer_parcial)
    return render(request, 'estudiantes/calificacion_1erparcial_edit.html', {'form_1erparcial': form_1erparcial})


def calculo_1erparcial(pk):
    calif_mono_x100 = Primer_parcial.objects.get(calif_mono,pk)*(0.6)
    return calif_mono_x100

