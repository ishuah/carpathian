CP.CompanyTemplate = _.template(""+
		"<div class='col-lg-3 text-center'>"+
            "<div class='thumbnail'>"+
                "<img src='<%= logo_url %>'>"+
                "<div class='caption'>"+
	                "<h3><%= name %></h3>"+
	                "<i><%= tagline %></i>"+
	                "<p><a href='/feedback/<%= id %>/' class='btn btn-primary'>Give feedback</a> <a href='/feedback/view/<%= id %>' class='btn btn-default' >View Feedback</p>"+
	            "</div>"+
            "</div>"+
        "</div>"+
	"")