from django import forms
from .models import Articulo, LONGITUD_MAXIMA



class FormArticulo(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = '__all__'
        # fields = ('nombre', 'precio')

        error_messages = {
            'nombre': {'max_length':LONGITUD_MAXIMA ,
            'required': 'Este campo es requerido'}
        }