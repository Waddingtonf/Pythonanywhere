from django.forms import ModelForm
from django import forms
from TCCApp.models import Upload

class UploadForm(ModelForm):
    imagem = forms.ImageField()
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'forms-nome',
        'placeholder': 'Insira o Nome da Imagem',
        'maxlength':'255'
        }))

    class Meta:
        model = Upload
        fields = ['imagem', 'nome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagem'].widget.attrs.update({'class': 'forms-img'})