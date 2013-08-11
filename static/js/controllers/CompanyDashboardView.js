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
		var view = this;
		if(confirm('are you sure you want to delete '+this.model.get('name'))){
			$.get('/delete/'+this.model.get('id')).success(function(){
				view.$el.fadeOut(1000);
			});
		}
	}
})