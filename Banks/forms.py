from Banks.models import Bank
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


CHOICES = (('','Please Select Consultancy Type'),('Retainer','Retainer'),('Project','Project'))

class BankForm(forms.ModelForm):

	consultants = forms.ModelMultipleChoiceField(label='Choose Consultants',queryset=User.objects.filter(is_consultant=True), 
		widget=forms.CheckboxSelectMultiple, required=True)
	spoc = forms.ModelChoiceField(empty_label="Select SPOC",queryset= User.objects.filter(is_consultant=True), widget=forms.Select, required=True)
	class Meta:
		model = Bank
		fields =[
            'name',
            'consultancy_type',
            'spoc',
            'consultants'
        ]



