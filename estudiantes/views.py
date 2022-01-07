from django.shortcuts import render
from .models import Alumnx
from .forms import AlumnxForm, Primer_parcialForm, Segundo_parcialForm, FinalForm, AutobiografiaForm

def lista_alumnx(request):
    alumnxs = Alumnx.objects.order_by('nombre')
    return render(request, 'estudiantes/lista_alumnx.html', {'alumnxs':alumnxs})

def alumnx_nuevo(request):
    form_alumnx = AlumnxForm
    return render(request, 'estudiantes/alumnx_edit.html', {'form_alumnx':form_alumnx})
