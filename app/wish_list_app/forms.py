from django import forms
from .models import Gift


class ReserveGift(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ["reserved_user"]


class FindMetaForm(forms.Form):
    html = forms.CharField(widget=forms.Textarea)
