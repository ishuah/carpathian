from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from carpathian.resources import CompanyResource, FeedbackResource

from django.contrib import admin
admin.autodiscover()

import backbone
backbone.autodiscover()

urlpatterns = patterns('',
     (r'^$', 'carpathian.views.index'),
     (r'^feedback/$', RedirectView.as_view(url='/')),
     (r'^feedback/(?P<companyID>[\d]{0,50})/$', 'carpathian.views.feedback'),
     (r'^feedback/view/(?P<companyID>[\d]{0,50})/$', 'carpathian.views.feedback_view'),
     (r'^employee/login/$', 'django.contrib.auth.views.login', {'template_name': 'carpathian/login.html'}),
     (r'^employee/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'carpathian/login.html'}),
     (r'^employee/dashboard/$', 'carpathian.views.employee_dashboard'),
     (r'^employee/dashboard/add/$', 'carpathian.views.add_company'),
     (r'^employee/dashboard/edit/(?P<companyID>[\d]{0,50})/$', 'carpathian.views.edit_company'),
     (r'^employee/dashboard/feedback/(?P<companyID>[\d]{0,50})/toggle/(?P<feedbackID>[\d]{0,50})/$', 'carpathian.views.edit_feedback'),
     (r'^employee/dashboard/feedback/(?P<companyID>[\d]{0,50})/$', 'carpathian.views.feedback_company'),
     (r'^employee/$', RedirectView.as_view(url='/employee/dashboard')),
     (r'^employee/dashboard/delete/(?P<companyID>[\d]{0,50})/$', 'carpathian.views.delete_company' ),
)
