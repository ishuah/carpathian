from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     (r'^$', 'carpathian.views.index'),
     (r'^feedback/$', RedirectView.as_view(url='/')),
     (r'^feedback/(?P<companyID>[\d]{0,50})/$', 'carpathian.views.feedback'),
     (r'^feedback/view/(?P<companyID>[\d]{0,50})/$', 'carpathian.views.feedback_view'),
     (r'^employee/login/$', 'django.contrib.auth.views.login', {'template_name': 'carpathian/login.html'}),
     (r'^employee/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'carpathian/login.html'}),
     (r'^employee/dashboard/$', 'carpathian.views.employee_dashboard'),
     (r'^employee/$', RedirectView.as_view(url='/employee/dashboard'))
)
