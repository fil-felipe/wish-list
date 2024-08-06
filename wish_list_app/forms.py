from django import forms
from .models import WishList, Gift


class AddWishList(forms.ModelForm):
    class Meta:
        model = WishList
        fields = ["list_name", "list_user"]

class AddWishListUser(forms.ModelForm):
    class Meta:
        model = WishList
        fields = ["list_name"]

class AddGift(forms.ModelForm):

    class Meta:
        model = Gift
        fields = ["gift_list", "title", "offer_url", "image_url"]

class AddGiftToList(forms.ModelForm):

    class Meta:
        model = Gift
        fields = ["title", "offer_url", "image_url"]

class ReserveGift(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ["id"]


class FindMetaForm(forms.Form):
    html = forms.CharField(widget=forms.Textarea)

