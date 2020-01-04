from django import forms
from Reports.models import Report,Q_Report
from django.forms import ModelForm
from Banks.models import Bank
from Classifications.models import Technology_domain,Document_type
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import SelectDateWidget
from django.forms.formsets import formset_factory
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone as tz
from tinymce.widgets import TinyMCE
from django.contrib.postgres.forms import SimpleArrayField
from django.contrib.auth import get_user_model
User = get_user_model()

class QFull_ReportForm(forms.Form):
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')

		super(QFull_ReportForm, self).__init__(*args, **kwargs)
		self.fields['consultants'].queryset = User.objects.filter(is_consultant=True).exclude(name=user)
		self.fields['spoc'].initial = User.objects.get(name=user)

	spoc=forms.CharField(label='SPOC',widget=forms.TextInput(attrs={'readonly':'readonly'}),)
	consultants = forms.ModelMultipleChoiceField(label='Choose Consultants',queryset=None, widget=forms.CheckboxSelectMultiple, required=True)
	bankname=forms.ModelChoiceField(label='Bankname',queryset=Bank.objects.all(),empty_label='Select Bank')
	From=forms.DateField(label='From Date',widget=forms.DateInput(attrs={'type':'date'}),required=True)
	To=forms.DateField(label='To Date',widget=forms.DateInput(attrs={'type':'date'}),required=True)

	requests_recieved = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 7}))
	summary_of_response = forms.CharField(widget=TinyMCE(attrs={'cols': 15, 'rows': 15}))
	summary_of_workdone = forms.CharField(widget=TinyMCE(attrs={'cols': 15, 'rows': 6}))
	learnings = forms.CharField(widget=TinyMCE(attrs={'cols': 15, 'rows': 6}))


class AttachmentsForm(forms.Form):
	file=forms.FileField(required=False,label='Upload File')
AttachmentsFormset= formset_factory(AttachmentsForm)

class QAForm(forms.Form):
	file=forms.FileField(required=False,label='Upload File')
QA_Formset= formset_factory(QAForm)

class CreateReportForm(forms.Form):
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')
		super(CreateReportForm, self).__init__(*args, **kwargs)
		self.fields['consultants'].queryset = User.objects.filter(is_consultant=True).exclude(name=user)
		self.fields['spoc'].initial = User.objects.get(name=user)
	spoc=forms.CharField(label='SPOC',widget=forms.TextInput(attrs={'readonly':'readonly'}),)
	consultants = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple, required=True)	
	bankname=forms.ModelChoiceField(queryset=Bank.objects.all(),required=True,empty_label='Select Bank')
	date=forms.DateField(label='Date',widget=forms.DateInput(attrs={'type':'date'}))
	topic= forms.CharField(max_length=200)
	technology_domain = forms.ModelChoiceField(label='Subject Area',queryset=Technology_domain.objects.all(),required=True,empty_label='Select Subject Area')
	document_type = forms.ModelChoiceField(label='Document Type',queryset=Document_type.objects.all(),required=True,empty_label='Select Document Type')
	query= forms.CharField(widget=TinyMCE(attrs={'cols': 15, 'rows': 10}))
	response= forms.CharField(widget=TinyMCE(attrs={'cols': 15, 'rows': 10}))
	q_attachments=forms.FileField(label='Query Attachments',widget=forms.FileInput(attrs={'multiple':True}))
	res_attachments=forms.FileField(label='Response Attachments',widget=forms.FileInput(attrs={'multiple':True}))
	


class SearchForm(forms.Form):
	bankname=forms.ModelChoiceField(label='Bankname',queryset=Bank.objects.all(),empty_label='Select Bank',required=True)
	From=forms.DateField(label='From Date',widget=forms.DateInput(attrs={'type':'date'}),required=True)
	To=forms.DateField(label='To Date',widget=forms.DateInput(attrs={'type':'date'}),required=True)

class TopicForm(forms.Form):
	topic=forms.CharField(label='Topic',widget=forms.TextInput(attrs={'placeholder':'Enter any keyword from Topic'}),)

class SubDocForm(forms.Form):
	technology_domain = forms.ModelChoiceField(label='Subject Area',queryset=Technology_domain.objects.all(),required=True,empty_label='Select Subject Area')
	document_type = forms.ModelChoiceField(label='Document Type',queryset=Document_type.objects.all(),required=True,empty_label='Select Document Type')

class ConsultantForm(forms.Form):
	consultant=forms.ModelChoiceField(label='SPOC or Consultant',empty_label='Select  ',widget=forms.Select,queryset = User.objects.filter(is_consultant=True))



# class ReportForm(ModelForm):
# 	def __init__(self, *args, **kwargs):
# 		user = kwargs.pop('user')
# 		super(ReportForm, self).__init__(*args, **kwargs)
# 		self.fields['spoc'].queryset = User.objects.filter(email=user)
# 		self.fields['consultants'].queryset = User.objects.filter(is_consultant=True).exclude(email=user)

# 	bankname=forms.ModelChoiceField(queryset=Bank.objects.all())
# 	consultants = forms.ModelMultipleChoiceField(queryset=None, widget=forms.SelectMultiple, required=True)
# 	spoc = forms.ModelChoiceField(queryset=None, widget=forms.Select, required=True)
# 	class Meta:
# 		model=Report
# 		fields=['spoc','consultants','date','bankname','topic','query','response']
# 		widgets = {	'query': forms.Textarea(attrs={'rows':3, 'cols':15}),
# 					'response':TinyMCE(attrs={'cols': 30, 'rows': 10}),
# 					#'response':forms.Textarea(attrs={'rows':3, 'cols':15,'id':'wysiwyg_editor'}),
# 					'date': forms.TextInput(attrs={'readonly':'readonly'})
# 				  }	


# class Q_ReportForm(forms.Form):
# 	def __init__(self, *args, **kwargs):
# 		user = kwargs.pop('user')
# 		super(Q_ReportForm, self).__init__(*args, **kwargs)
# 		self.fields['consultants'].queryset = User.objects.filter(is_consultant=True).exclude(email=user)
# 		self.fields['spoc'].initial = User.objects.get(email=user)
# 	spoc=forms.CharField(label='SPOC',widget=forms.TextInput(attrs={'readonly':'readonly'}),)
# 	consultants = forms.ModelMultipleChoiceField(queryset=None, widget=forms.SelectMultiple, required=True)
# 	bankname=forms.ModelChoiceField(label='Bankname',queryset=Bank.objects.all(),empty_label='Select Bank')
# 	From=forms.DateField(label='From Date',widget=forms.DateInput(attrs={'type':'date'}),required=True)
# 	To=forms.DateField(label='To Date',widget=forms.DateInput(attrs={'type':'date'}),required=True)
	# requests_recieved = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':15}))
	# summary_of_response = forms.CharField(widget=forms.Textarea(attrs={'rows':7, 'cols':15}))
	# summary_of_workdone = forms.CharField(widget=forms.Textarea(attrs={'rows':7, 'cols':15}))	
	# learnings = forms.CharField(widget=forms.Textarea(attrs={'rows':7, 'cols':15}))

