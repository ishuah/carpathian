CP.Workspace = Backbone.Router.extend({

	 routes: {
        '': 'index'
    },

    index: function(){
        this.navigate('/feedback/6');
    }
})