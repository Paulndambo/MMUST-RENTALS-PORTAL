from django import forms
from .models import Owner, Rental


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ["name", "email", "phone_number"]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
