from django import forms
from feedback import Feedback
from companies import Company
from form_utils.fields import ClearableImageField
from form_utils.widgets import ImageWidget

class FeedbackForm(forms.ModelForm):

	customer_firstname = forms.CharField(label="First name", required=True)
	customer_lastname = forms.CharField(label="Last name", required=True)
	customer_email = forms.EmailField(label="Email", required=True)
	comments = forms.CharField(widget=forms.Textarea, label='Comments', required=True)
	show_name_public = forms.BooleanField(label="Allow others to see your name", required=False)
	class Meta():
		model = Feedback
		fields = ('customer_firstname', 'customer_lastname', 'customer_email', 'comments', 'show_name_public')


class CompanyForm(forms.ModelForm):
	name = forms.CharField(label="Company name", required=True)
	tagline = forms.CharField(label="Tagline", required=True)
	description = forms.CharField(label="Description", required=True)
	logo = forms.ImageField(widget=ImageWidget) #forms.ImageField(label="Logo", required=True)

	class Meta():
		model = Company
		fields = ('name', 'tagline', 'description', 'logo')