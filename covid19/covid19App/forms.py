from django import forms

class PostcodeForm(forms.Form):
    postcode = forms.CharField()