from django import forms
from .models import Polyabron
from django.utils import timezone
class PolyabronForm(forms.ModelForm):
    class Meta:
        model = Polyabron
        fields = '__all__'
        widgets = {
            'kun': forms.DateInput(attrs={'type': 'date', 'min': str(timezone.now().date())}),
            'vaqti': forms.TimeInput(attrs={'type': 'time'}),
        }
