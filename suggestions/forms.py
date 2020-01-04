from suggestions.models import Suggestion
from django import forms


class SForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={'rows':6, 'cols':15}),label='')

	class Meta:
		model = Suggestion
		fields =[ 'content',]



