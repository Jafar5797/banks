from Classifications.models import Technology_domain,Document_type
from django import forms

class TForm(forms.ModelForm):
    class Meta :
        model = Technology_domain
        fields =[
            'name',
        ]


class DForm(forms.ModelForm):
    class Meta :
        model = Document_type
        fields =[
            'name',
        ]


class TestForm(forms.Form):
    attachments=forms.FileField(label='Query Attachments',widget=forms.FileInput(
        attrs={'name':'addmore[]','class':'form-control'}))
