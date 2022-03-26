from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumnx, Primer_parcial, Segundo_parcial, Final, Autobiografia
from .forms import AlumnxForm, Primer_parcialForm, Segundo_parcialForm, FinalForm, AutobiografiaForm, Primer_parcial_edit_Form, Segundo_parcial_edit_Form, Final_edit_Form, Autobiografia_edit_Form
from django.contrib import messages
from django.db.models.functions import Coalesce
from decimal import Decimal
from django.db.models import F
from django.forms.models import model_to_dict


def lista_alumnx(request):
    alumnxs = Alumnx.objects.order_by('nombre')
    alumnos_modificados = []
    for alumn in alumnxs:
        alumno = model_to_dict(alumn)
        calif = alumn.primer_par.first()
        if calif:
            alumno['calif'] = calif.promedio
        alumnos_modificados.append(alumno)
    return render(request, 'estudiantes/lista_alumnx.html', {'alumnxs':alumnos_modificados})


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
                                                    promedio_1erparcial=(F('calif_mono')*Decimal(.6))+
                                                    (F('calif_expo_1er')*Decimal(.1))+
                                                    (F('participacion_1er')*Decimal(.3))).order_by('nombre')
    
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
        form_1erparcial = Primer_parcial_edit_Form(request.POST, instance=primer_parcial)
        if form_1erparcial.is_valid():
            primer_parcial = form_1erparcial.save()
            primer_parcial.save()
            return redirect('lista_calif1erpar')
    else:
        form_1erparcial = Primer_parcial_edit_Form(instance=primer_parcial)
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
        form_2doparcial = Segundo_parcial_edit_Form(request.POST, instance=segundo_parcial)
        if form_2doparcial.is_valid():
            segundo_parcial = form_2doparcial.save()
            segundo_parcial.save()
            return redirect('lista_calif2dopar')
    else:
        form_2doparcial = Segundo_parcial_edit_Form(instance=segundo_parcial)
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
        form_finalparcial = Final_edit_Form(request.POST, instance=final_parcial)
        if form_finalparcial.is_valid():
            final_parcial = form_finalparcial.save()
            final_parcial.save()
            return redirect('lista_calif_final')
    else:
        form_finalparcial = Final_edit_Form(instance=final_parcial)
    return render(request, 'estudiantes/calificacion_finalparcial_edit.html', {'form_finalparcial': form_finalparcial})

def lista_autobiografia(request):
    autobiografias = Autobiografia.objects.order_by('nombre')
    print("hola")
    
    return render(request, 'estudiantes/lista_autobiografia.html', {'autobiografias':autobiografias})

def autobiografia(request):
    if request.method == "POST":
        form_autobiografia = AutobiografiaForm(request.POST)
        print("hola 2")
 
        if form_autobiografia.is_valid():
            autobiografia = form_autobiografia.save()
            autobiografia.save()
            print("hola 3")
            return redirect('lista_autobiografia')
    else:
        form_autobiografia = AutobiografiaForm()
        print("hola 4")
    return render(request, 'estudiantes/calificacion_autobiografia_edit.html', {'form_autobiografia':form_autobiografia})

def autobiografia_edit(request, pk):
    autobiografia = get_object_or_404(Autobiografia, pk=pk)
    if request.method == "POST":
        form_autobiografia = Autobiografia_edit_Form(request.POST, instance=autobiografia)
        if form_autobiografia.is_valid():
            autobiografia = form_autobiografia.save()
            autobiografia.save()
            return redirect('lista_autobiografia')
    else:
        form_autobiografia = Autobiografia_edit_Form(instance=autobiografia)
    return render(request, 'estudiantes/calificacion_autobiografia_edit.html', {'form_autobiografia': form_autobiografia})
