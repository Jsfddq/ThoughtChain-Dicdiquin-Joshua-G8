from django import forms
from .models import Node

class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }