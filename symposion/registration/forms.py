from django import forms
from symposion.registration.models import Registrant


class RegistrantForm(forms.ModelForm):
    
    
    class Meta:
        exclude = ["user",]
        model = Registrant
