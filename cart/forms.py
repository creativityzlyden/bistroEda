from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.BooleanField()
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
