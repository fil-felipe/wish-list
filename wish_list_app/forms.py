from django import forms

class FindMetaForm(forms.Form):
    html = forms.CharField(widget=forms.Textarea)