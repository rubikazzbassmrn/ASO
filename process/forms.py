#Importar ModelForm
from django import forms
#Importar modelo Operator
from .models import Operators, Operator_information, Documentation

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
            'id_status'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name_p': forms.TextInput(attrs={'class':'form-control'}),
            'last_name_m': forms.TextInput(attrs={'class':'form-control'}),
            'b_day': forms.DateInput(attrs={'type':'date'}),
            'rfc': forms.TextInput(attrs={'class':'form-control'}),
            'curp': forms.TextInput(attrs={'class':'form-control'}),
            'id_state': forms.Select(attrs={'class':'form-control'}),#Colocamos la clase 'select2' para usar el plugin select2
            'id_town': forms.Select(attrs={'class':'form-control'}),
            'id_marital_status': forms.Select(attrs={'class':'form-control'}),
            'id_education_level': forms.Select(attrs={'class':'form-control'}),
            'id_status': forms.Select(attrs={'class':'form-control', 'value':'activo'})
        }

class OpinfoForm(forms.ModelForm):

    class Meta:
        model = Operator_information

        fields = [
            'id_operator',
            'id_media',
            'id_mexa_interest',
            'id_truck_type',
            'last_job',
            'period_started',
            'period_finished',
            'id_status_job',
            'actual_job_where',
            'id_status_process',
            'actual_process_where',
            'id_status'
        ]
        widgets = {
            'id_operator': forms.Select(attrs={'class':'form-control'}),
            'id_media': forms.Select(attrs={'class':'form-control'}),
            'id_mexa_interest': forms.Select(attrs={'class':'form-control'}),
            'id_truck_type': forms.CheckboxSelectMultiple(),
            'last_job': forms.TextInput(attrs={'class':'form-control'}),
            'period_started': forms.DateInput(attrs={'type':'date'}),
            'period_finished': forms.DateInput(attrs={'type':'date'}),
            'id_status_job': forms.Select(attrs={'class':'form-control'}),
            'actual_job_where': forms.TextInput(attrs={'class':'form-control'}),
            'id_status_process': forms.Select(attrs={'class':'form-control'}),
            'actual_process_where': forms.TextInput(attrs={'class':'form-control'}),
            'id_status': forms.Select(attrs={'class':'form-control'})
        }

class DocumentsForm(forms.ModelForm):

    class Meta:
        model = Documentation

        fields = [
            'id_operator',
            'curp_file',
            'secure_number_file',
            'secure_number',
            'licence_file',
            'licence',
            'licence_started',
            'licence_finished',
            'psicofisico_file',
            'recommendation_letter_file'
        ]
        widgets = {
            'id_operator': forms.Select(attrs={'class':'form-control'}),
            #'curp_file': forms.FileField(),
            #'secure_number_file': forms.FileField(),
            'secure_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresa el numero de seguro'}),
            #'licence_file': forms.FileField(),
            'licence': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresa el numero de licencia'}),
            'licence_started': forms.DateInput(attrs={'type':'date'}),
            'licence_finished': forms.DateInput(attrs={'type':'date'}),
            #'psicofisico_file': forms.FileField(),
            #'recommendation_letter_file': forms.FileField()
        }