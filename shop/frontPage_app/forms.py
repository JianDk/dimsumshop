from django import forms
from .models import customerLocation

class addressForm(forms.ModelForm):
    class Meta:
        model = customerLocation

        fields = [
            'postnr',
        ]
