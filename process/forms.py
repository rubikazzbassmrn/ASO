#Importar ModelForm
from django.forms import ModelForm
#Importar modelo Operator
from operators.models import Operators

class GeneralForm(ModelForm):

    class Meta:
        model = Operators
        fields = ['first_name', 'last_name_p', 'last_name_m', 'b_day', 'rfc', 'curp']
