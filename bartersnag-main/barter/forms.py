from django import forms

from .models import Barter
from .models import Category, Barter

INPUT_CLASSES = 'login'

class NewBarterForm(forms.ModelForm):
    class Meta:
        model = Barter
        fields = ('category', 'name', 'description', 'exchange_item', 'image', 'location')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'exchange_item': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'location': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
        }