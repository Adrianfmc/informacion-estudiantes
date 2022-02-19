from django import forms
from .models import Alumnx, Primer_parcial, Segundo_parcial, Final, Autobiografia

class AlumnxForm(forms.ModelForm):

    class Meta:
        model = Alumnx
        fields = ('nombre', 'num_cuenta', 'email', 'universidad', 'asignatura', 'ciclo',)

class Primer_parcialForm(forms.ModelForm):

    class Meta:
        model = Primer_parcial
        fields = ('nombre', 'calif_mono', 'calif_expo_1er', 'participacion_1er',)

class Segundo_parcialForm(forms.ModelForm):

    class Meta:
        model = Segundo_parcial
        fields = ('calif_ensay_2do', 'calif_expo_2do', 'participacion_2do',)

class FinalForm(forms.ModelForm):

    class Meta:
        model = Final
        fields = ('calif_ensay_final', 'calif_expo_final', 'participacion_final',)

class AutobiografiaForm(forms.ModelForm):

    class Meta:
        model = Autobiografia
        fields = ('autobiografia',)
