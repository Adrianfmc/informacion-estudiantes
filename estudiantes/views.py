from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumnx
from .forms import AlumnxForm, Primer_parcialForm, Segundo_parcialForm, FinalForm, AutobiografiaForm


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
