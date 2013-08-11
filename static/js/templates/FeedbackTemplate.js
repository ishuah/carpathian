CP.FeedbackTemplate = _.template(""+
			"<div class='panel'>"+
			"<p><%= comments %></p> <p class='text-right'>by <%= user %></p>"+
			"<p><% if (approved == 'True') { %>"+
			"<i class='text-success'>This comment is approved</i>"+
			"<a href='toggle/<%= id %>' class='btn btn-danger pull-right'>Deny</a>"+
			"<% } %>"+
			"<% if(approved == 'False') { %>"+
			"<i class='text-danger'>This comment is not approved</i>"+
			"<a href='toggle/<%= id %>' class='btn btn-success pull-right'>Approve</a>"+
			"<% } %>"+
			"</p>"+
			"</div>"+
		"")