from django.forms import ModelForm
from django import forms

from ordenamiento.models import Parroquia, \
        Barrio

class ParroquiaForm(forms.ModelForm): 
    class Meta:
        model = Parroquia 
        fields = ['nombre', 'tipo_parroquia'] 

class BarrioForm(forms.ModelForm): 
    class Meta:
        model = Barrio 
        fields = ['nombre', 'num_viviendas', 'parques','num_edificios','parroquia'] 

class BarrioParroquiaForm(forms.ModelForm): 
    
    def __init__(self, parroquia, *args, **kwargs):
        super(BarrioParroquiaForm, self).__init__(*args, **kwargs)
        self.initial['parroquia'] = parroquia
        self.fields["parroquia"].widget = forms.widgets.HiddenInput()
        print(parroquia)
    
    class Meta:
        model = Barrio 
        fields = ['nombre', 'num_viviendas', 'parques','num_edificios','parroquia'] 