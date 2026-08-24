from django import forms
from .models import Visit
class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'
        widgets = {
            'diagnosis': forms.Textarea(attrs={'rows':3}),
            'treatment': forms.Textarea(attrs={'rows':3}),
            'prescription': forms.Textarea(attrs={'rows':3}),
            'notes': forms.Textarea(attrs={'rows':3}),
        }
