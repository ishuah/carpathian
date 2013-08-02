from django import forms
from feedback import Feedback

class FeedbackForm(forms.ModelForm):

	customer_firstname = forms.CharField(label="First name", required=True)
	customer_lastname = forms.CharField(label="Last name", required=True)
	customer_phone_num = forms.IntegerField(label="Phone number", required=True)
	comments = forms.CharField(widget=forms.Textarea, label='Comments', required=True)

	class Meta():
		model = Feedback
		fields = ('customer_firstname', 'customer_lastname', 'customer_phone_num', 'comments')