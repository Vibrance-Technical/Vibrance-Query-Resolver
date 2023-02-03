from . models import *
from django import forms

class SearchReferenceForm(forms.ModelForm):
    slug = forms.CharField(label = "Reference ID",help_text = "Enter the Reference ID Sent to the respective mail id")
    class Meta:
        model = Query
        fields = ['slug']
