from django import forms
from controller.models import Transacao, ImportacaoRealizada
from django.core.validators import FileExtensionValidator


class FormFileUpload(forms.Form):

    arquivo = forms.FileField(validators=[FileExtensionValidator(['csv'])])


class FormImportacoesRealizadas(forms.ModelForm):
    class Meta:
        model = ImportacaoRealizada
        fields = '__all__'

