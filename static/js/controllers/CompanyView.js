CP.CompanyView = Backbone.View.extend({

	initialize: function(){
		this.render();
	},

	render: function(){
		this.setElement(CP.CompanyTemplate(this.model.toJSON()));
		$('#company-list').append(this.$el);
	}
})