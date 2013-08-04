CP.CompanyDashboardView = Backbone.View.extend({

	events: {
		"click .btn-danger": "deleteCompany"
	},
	
	initialize: function(){
		this.render();
	},

	render: function(){
		this.setElement(CP.CompanyDashboardTemplate(this.model.toJSON()));
		$('#company-table tbody').append(this.$el);
	},

	deleteCompany: function(){
		this.$el.fadeOut(1000).remove();
	}
})