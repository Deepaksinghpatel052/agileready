from django import forms
from .models import import_files_data

class ImportFilesDataForm(forms.ModelForm):
    files = forms.FileField(required=False)
    class Meta:
        model = import_files_data
        fields = ['files']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['files'].widget.attrs={"class": "form-control"}
