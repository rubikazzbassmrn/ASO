#Importar ModelForm
from django import forms
#Importar modelo Operator
from .models import Operators

class OperatorForm(forms.ModelForm):

    class Meta:
        model = Operators

        fields = [
            'first_name',
            'last_name_p',
            'last_name_m',
            'b_day',
            'rfc',
            'curp',
            'id_state',
            'id_town',
            'id_marital_status',
            'id_education_level',
            'id_status',
        ]
        labels = {
            'first_name': 'Ingresa nombre(s)',
            'last_name_p': 'Ingresa apellido paterno',
            'last_name_m': 'Ingresa apellido materno',
            'b_day': 'Fecha de nacimiento',
            'rfc': 'Ingresa RFC',
            'curp': 'Ingresa CURP',
            'id_state': 'Seleccione estado',
            'id_town': 'Seleccione municipio',
            'id_marital_status': 'Estado civil',
            'id_education_level': 'Máximo grado de estudios',
            'id_status': 'Status',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name_p': forms.TextInput(attrs={'class':'form-control'}),
            'last_name_m': forms.TextInput(attrs={'class':'form-control'}),
            'b_day': forms.DateInput(attrs={'class':'form-control'}),
            'rfc': forms.TextInput(attrs={'class':'form-control'}),
            'curp': forms.TextInput(attrs={'class':'form-control'}),
            'id_state': forms.Select(attrs={'class':'form-control'}),
            'id_town': forms.Select(attrs={'class':'form-control'}),
            'id_marital_status': forms.Select(attrs={'class':'form-control'}),
            'id_education_level': forms.Select(attrs={'class':'form-control'}),
            'id_status': forms.Select(attrs={'class':'form-control'})
        }
        
