from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from carpathian.models import Company, Feedback, FeedbackForm
from django.utils.html import strip_tags

def index(request):
	companies = Company.objects.all()
	return render(request, 'carpathian/index.html', {'companies': companies })

def feedback(request, companyID=None):
	company = Company.objects.get(pk=companyID)
	page_title = "Company Feedback Page"

	if request.method == 'POST':
		feedback_form = FeedbackForm(request.POST)
		if feedback_form.is_valid():
			feedback = feedback_form.save(commit=False)
			feedback.company = company
			feedback.comments = strip_tags(feedback_form.cleaned_data['comments'])
			feedback.save()
			feedback_form = FeedbackForm()
			return render(request, 'carpathian/feedback.html', {'page_title': page_title, 'company': company, 'feedback_form': feedback_form, 'message': 'Your feedback has been received, thank you!' })

		return render(request, 'carpathian/feedback.html', {'page_title': page_title, 'company': company, 'feedback_form': feedback_form })
	else:
		feedback_form = FeedbackForm()
		return render(request, 'carpathian/feedback.html', {'page_title': page_title, 'company': company, 'feedback_form': feedback_form })

def feedback_view(request, companyID=None):
	company = Company.objects.get(pk=companyID)
	feedback = Feedback.objects.filter(company=company)

	return render(request, 'carpathian/feedback_view.html', { 'feedback':feedback, 'company': company })

@login_required
def employee_dashboard(request):
	employee_companies = Company.objects.filter(employee=request.user)
	return render(request, 'carpathian/dashboard.html', {'companies': employee_companies})