CP.FeedbackView = Backbone.View.extend({

	initialize: function(){
		this.render();
	},

	render: function(){
		this.setElement(CP.FeedbackTemplate(this.model.toJSON()));
		$('#feedback-list').append(this.$el);
	}
})