CP.Company = Backbone.Model.extend({

}, 
{
	create: function(id, name, tagline, description, logo_url){
		var company = new CP.Company({ id:id, name:name, tagline: tagline, description:description, logo_url:logo_url });
		CP.companylist.add(company);

		return company;
	}
});

CP.CompanyList = Backbone.Collection.extend({
	model: CP.Company,
});

CP.companylist = new CP.CompanyList();