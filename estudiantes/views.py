from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumnx, Primer_parcial, Segundo_parcial, Final
from .forms import AlumnxForm, Primer_parcialForm, Segundo_parcialForm, FinalForm, AutobiografiaForm
from django.contrib import messages
from django.db.models.functions import Coalesce
from decimal import Decimal
from django.db.models import F


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
    primer_parcials = Primer_parcial.objects.annotate(calif_mono60=F('calif_mono')*Decimal(.6),
                                                    calif_expo_1er10=F('calif_expo_1er')*Decimal(.1),
                                                    participacion_1er30=F('participacion_1er')*Decimal(.3),
                                                    promedio_1erparcial=(F('calif_mono')*Decimal(.6))+(F('calif_expo_1er')*Decimal(.1))+(F('participacion_1er')*Decimal(.3))).order_by('nombre')
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

def lista_calif2dopar(request):
    segundo_parcials = Segundo_parcial.objects.annotate(calif_ensayo_2do60=F('calif_ensay_2do')*Decimal(.6),
                                                    calif_expo_2do10=F('calif_expo_2do')*Decimal(.1),
                                                    participacion_2do30=F('participacion_2do')*Decimal(.3),
                                                    promedio_2doparcial=(F('calif_ensay_2do')*Decimal(.6))+
                                                    (F('calif_expo_2do')*Decimal(.1))+(F('participacion_2do')*Decimal(.3))).order_by('nombre')
    return render(request, 'estudiantes/lista_calif2dopar.html', {'segundo_parcials':segundo_parcials})

def segundo_parcial(request):
    if request.method == "POST":
        form_2doparcial = Segundo_parcialForm(request.POST)
        if form_2doparcial.is_valid():
            segundo_parcial = form_2doparcial.save()
            segundo_parcial.save()
            return redirect('lista_calif2dopar')
    else:
        form_2doparcial = Segundo_parcialForm()
    return render(request, 'estudiantes/calificacion_2doparcial_edit.html', {'form_2doparcial':form_2doparcial})

def segundo_parcial_edit(request, pk):
    segundo_parcial = get_object_or_404(Segundo_parcial, pk=pk)
    if request.method == "POST":
        form_2doparcial = Segundo_parcialForm(request.POST, instance=segundo_parcial)
        if form_2doparcial.is_valid():
            segundo_parcial = form_2doparcial.save()
            segundo_parcial.save()
            return redirect('lista_calif2dopar')
    else:
        form_2doparcial = Segundo_parcialForm(instance=segundo_parcial)
    return render(request, 'estudiantes/calificacion_2doparcial_edit.html', {'form_2doparcial': form_2doparcial})

def lista_calif_final(request):
    final_parcials = Final.objects.annotate(calif_ensayo_final60=F('calif_ensay_final')*Decimal(.6),
                                                    calif_expo_final0=F('calif_expo_final')*Decimal(.1),
                                                    participacion_final30=F('participacion_final')*Decimal(.3),
                                                    promedio_final_parcial=(F('calif_ensay_final')*Decimal(.6))+
                                                    (F('calif_expo_final')*Decimal(.1))+(F('participacion_final')*Decimal(.3))).order_by('nombre')
    return render(request, 'estudiantes/lista_calif_final_par.html', {'final_parcials':final_parcials})

def final_parcial(request):
    if request.method == "POST":
        form_finalparcial = FinalForm(request.POST)
        if form_finalparcial.is_valid():
            final_parcial = form_finalparcial.save()
            final_parcial.save()
            return redirect('lista_calif_final')
    else:
        form_finalparcial = FinalForm()
    return render(request, 'estudiantes/calificacion_finalparcial_edit.html', {'form_finalparcial':form_finalparcial})

def final_parcial_edit(request, pk):
    final_parcial = get_object_or_404(Final, pk=pk)
    if request.method == "POST":
        form_finalparcial = FinalForm(request.POST, instance=final_parcial)
        if form_finalparcial.is_valid():
            final_parcial = form_finalparcial.save()
            final_parcial.save()
            return redirect('lista_calif_final_par')
    else:
        form_finalparcial = FinalForm(instance=final_parcial)
    return render(request, 'estudiantes/calificacion_finalparcial_edit.html', {'form_finalparcial': form_finalparcial})