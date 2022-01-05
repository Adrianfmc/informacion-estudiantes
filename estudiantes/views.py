from django.shortcuts import render

def lista_alumnx(request):
    return render(request, 'estudiantes/lista_alumnx.html', {})
