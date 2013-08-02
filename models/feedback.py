from companies import Company
from django.db import models

class Feedback(models.Model):
	customer_firstname = models.CharField(max_length=30, blank=False)
	customer_lastname = models.CharField(max_length=30, blank=False)
	customer_phone_num = models.IntegerField(max_length=10, blank=False)
	comments = models.TextField(blank=False)

	#one to many relation to the company
	company = models.ForeignKey(Company)

	class Meta:
		app_label = "carpathian"
		db_table = "carpathian_feedback"
		verbose_name_plural = "feedback"

	def __unicode__(self):
		return self.customer_firstname+" "+self.customer_lastname+" on "+self.company.name
