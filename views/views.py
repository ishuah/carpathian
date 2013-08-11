from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from carpathian.models import Company, Feedback, FeedbackForm, CompanyForm
from django.utils.html import strip_tags

def index(request):
	companies = Company.objects.all()
	return render(request, 'carpathian/index.html', {'companies': companies })

def feedback(request, companyID=None):
	company = get_object_or_404(Company, pk=companyID)

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
	company = get_object_or_404(Company, pk=companyID)

	feedback = Feedback.objects.filter(company=company)

	return render(request, 'carpathian/feedback_view.html', { 'feedback':feedback, 'company': company })

@login_required(login_url="/employee/login/?next=/watsan")
def employee_dashboard(request):
	employee_companies = Company.objects.filter(employee=request.user)
	return render(request, 'carpathian/dashboard.html', {'companies': employee_companies})

@login_required
def delete_company(request, companyID=None):
	company = get_object_or_404(Company, pk=companyID)
	company.delete()

	return HttpResponse(status=200)

@login_required
def add_company(request):
	if request.method == 'POST':
		company_form = CompanyForm(data=request.POST, files=request.FILES)
		if company_form.is_valid():
			company = company_form.save(commit=False)
			company.employee = request.user
			company.save()
			return redirect('/employee/dashboard/')

		return render(request, 'carpathian/add_company.html', { 'company_form': company_form })
	else:
		company_form = CompanyForm()
		return render(request, 'carpathian/add_company.html', { 'company_form': company_form })

@login_required
def edit_company(request, companyID=None):
	company = get_object_or_404(Company, pk=companyID)

	if request.method == 'POST':
		company_form = CompanyForm(data=request.POST, files=request.FILES, instance=company)
		if company_form.is_valid():
			company_form.save()
			return redirect('/employee/dashboard/')
		else:
			return render(request, 'carpathian/edit_company.html', { 'company':company, 'company_form': company_form })
	else:
		company_form = CompanyForm(instance=company)
		return render(request, 'carpathian/edit_company.html', { 'company':company, 'company_form': company_form })

@login_required
def feedback_company(request, companyID=None):
	company = get_object_or_404(Company, pk=companyID)

	feedback = Feedback.objects.filter(company=company)

	return render(request, 'carpathian/dashboard_feedback_view.html', { 'feedback':feedback, 'company': company })
