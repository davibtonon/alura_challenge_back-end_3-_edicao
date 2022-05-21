from django.forms import ModelForm, forms
from controller.models import ImportacaoRealizada
from django.core.validators import FileExtensionValidator

class FormFileUpload(forms.Form):

    arquivo = forms.FileField(validators=[FileExtensionValidator(['csv', 'xml'])])


class FormImportacoesRealizadas(ModelForm):
    class Meta:
        model = ImportacaoRealizada
        fields = '__all__'
