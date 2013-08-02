from django.db import models
from django.contrib.auth.models import User 

class Company(models.Model):
	name = models.CharField(max_length=100, blank=False)
	tagline = models.CharField(max_length=100, blank=False)
	description = models.CharField(max_length=300, blank=False)
	logo = models.ImageField(upload_to="logos", blank=False, null=False)

	#one to many relation to the employees
	employee = models.ForeignKey(User)

	class Meta:
		app_label = "carpathian"
		db_table = "carpathian_companies"
		verbose_name_plural = "companies"

	def __unicode__(self):
		return self.name
			