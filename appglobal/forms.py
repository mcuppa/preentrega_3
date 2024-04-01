from django import forms
from .models import *

class PinturasForm(forms.ModelForm):
    class Meta:
        model = Pinturas
        fields = ['name', 'color', 'litros']
        

class AccesoriosForm(forms.ModelForm):
    class Meta:
        model = Accesorios
        fields = ['description', 'brand', 'type', 'material']
        
class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['name', 'adress', 'condition', 'location']