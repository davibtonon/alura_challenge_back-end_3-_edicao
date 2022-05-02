from django.forms import ModelForm, forms
from controller.models import ImportacaoRealizada
from django.core.validators import FileExtensionValidator

class FormFileUpload(forms.Form):

    arquivo = forms.FileField(validators=[FileExtensionValidator(['csv'])])


class FormImportacoesRealizadas(ModelForm):
    class Meta:
        model = ImportacaoRealizada
        fields = '__all__'
