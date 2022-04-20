from django import forms
from controller.models import Transacao
from django.core.validators import FileExtensionValidator


class FormFileUpload(forms.Form):

    arquivo = forms.FileField(validators=[FileExtensionValidator(['csv'])])


class TranscaoForms(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = '__all__'

     