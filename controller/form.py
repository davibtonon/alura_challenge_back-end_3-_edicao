from django import forms

class FormFileUpload(forms.Form):

    arquivo = forms.FileField()
    