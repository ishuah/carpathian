CP.CompanyDashboardTemplate = _.template(""+
		"<tr>"+
            "<td><%= name %></td>"+
            "<td><button class='btn btn-danger'>delete</button></td>"+
            "<td><button class='btn btn-primary'>edit</button></td>"+
            "<td><button class='btn btn-info'>feedback</button></td>"+
        "</tr>"+
	"")