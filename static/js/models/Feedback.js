CP.Feedback = Backbone.Model.extend({

}, 
{
	create: function(user, comments){
		var feedback = new CP.Feedback({ user:user, comments:comments });
		CP.feedbackList.add(feedback);

		return feedback;
	}
});

CP.FeedbackList = Backbone.Collection.extend({
	model: CP.Feedback,
});

CP.feedbackList = new CP.FeedbackList();