import backbone
from carpathian.models import *

class CompanyAPIView(backbone.views.BackboneAPIView):
	model = Company
	display_fields = ('name', 'tagline','description', 'logo')

backbone.site.register(CompanyAPIView)