from . models import *
from django import forms

class SearchReferenceForm(forms.ModelForm):
    slug = forms.CharField(label = "Reference ID",help_text = "Enter the Reference ID Sent to the respective mail id")
    class Meta:
        model = Query
        fields = ['slug']

class QueryCreateForm(forms.ModelForm):
    user_name = forms.CharField(help_text = "Username registered in VITC Events")
    registration_id = forms.CharField(help_text = "Registration Id registered in VITC Events",label = "Registration Number")
    email = forms.EmailField(help_text = "Reference ID of the Query will be sent to this mail id",required = True)
    screenshot = forms.FileField(label = "Reference Documents")
    
    class Meta:
        model = Query
        fields = ["user_name","registration_id","email","college_name","title","event_name","description","order_id","screenshot"]