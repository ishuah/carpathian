from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from carpathian.models import Company, FeedbackForm

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
			feedback.save()
			feedback_form = FeedbackForm()
			return render(request, 'carpathian/feedback.html', {'page_title': page_title, 'company': company, 'feedback_form': feedback_form, 'message': 'Your feedback has been received, thank you!' })

		return render(request, 'carpathian/feedback.html', {'page_title': page_title, 'company': company, 'feedback_form': feedback_form })
	else:
		feedback_form = FeedbackForm()
		return render(request, 'carpathian/feedback.html', {'page_title': page_title, 'company': company, 'feedback_form': feedback_form })

@login_required
def employee_dashboard(request):
	employee_companies = Company.objects.filter(employee=request.user)
	return render(request, 'carpathian/dashboard.html', {'companies': employee_companies})