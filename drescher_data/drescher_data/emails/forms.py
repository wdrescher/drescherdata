from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    body = forms.CharField(widget = forms.Textarea)
    class Meta:
        model =  Contact
        exclude = []
