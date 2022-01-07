from django.shortcuts import render
from .forms import AlumnxForm, Primer_parcialForm, Segundo_parcialForm, FinalForm, AutobiografiaForm

def lista_alumnx(request):
    return render(request, 'estudiantes/lista_alumnx.html', {})

def alumnx_nuevo(request):
    form = AlumnxForm
    return render(request, 'estudiantes/alumnx_edit.html', {'form':form})
