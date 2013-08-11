CP.CompanyDashboardTemplate = _.template(""+
		"<tr>"+
            "<td><%= name %></td>"+
            "<td><button class='btn btn-danger'>delete</button></td>"+
            "<td><a href='/employee/dashboard/edit/<%= id %>' class='btn btn-primary'>edit</a></td>"+
            "<td><a href='/employee/dashboard/feedback/<%= id %>' class='btn btn-info'>feedback</a></td>"+
        "</tr>"+
	"")