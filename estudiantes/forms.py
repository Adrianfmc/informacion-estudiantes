from django import forms
from .models import Alumnx, Primer_parcial, Segundo_parcial, Final, Autobiografia
from django.core.exceptions import ValidationError

class AlumnxForm(forms.ModelForm):

    class Meta:
        model = Alumnx
        fields = ('nombre', 'num_cuenta', 'email', 'universidad', 'asignatura', 'ciclo',)

class Primer_parcialForm(forms.ModelForm):

    class Meta:
        model = Primer_parcial
        fields = ('nombre', 'calif_mono', 'calif_expo_1er', 'participacion_1er',)
    
    def clean(self):
        
        clean_data=super().clean()
        nombre = clean_data.get("nombre")
        if Primer_parcial.objects.filter(nombre = clean_data.get("nombre")):
            raise ValidationError("Ya está calificadx este alumnx")
        return clean_data

class Segundo_parcialForm(forms.ModelForm):

    class Meta:
        model = Segundo_parcial
        fields = ('nombre','calif_ensay_2do', 'calif_expo_2do', 'participacion_2do',)

    def clean(self):
        
        clean_data=super().clean()
        nombre = clean_data.get("nombre")
        if Segundo_parcial.objects.filter(nombre = clean_data.get("nombre")):
            raise ValidationError("Ya está calificadx este alumnx")
        return clean_data

class FinalForm(forms.ModelForm):

    class Meta:
        model = Final
        fields = ('nombre','calif_ensay_final', 'calif_expo_final', 'participacion_final',)
    
    def clean(self):
        
        clean_data=super().clean()
        nombre = clean_data.get("nombre")
        if Final.objects.filter(nombre = clean_data.get("nombre")):
            raise ValidationError("Ya está calificadx este alumnx")
        return clean_data

class AutobiografiaForm(forms.ModelForm):

    class Meta:
        model = Autobiografia
        fields = ('nombre','autobiografia',)
    
    def clean(self):
        
        clean_data=super().clean()
        nombre = clean_data.get("nombre")
        if Autobiografia.objects.filter(nombre = clean_data.get("nombre")):
            raise ValidationError("Ya está calificadx este alumnx")
        return clean_data
