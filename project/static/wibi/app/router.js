import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.resource('message', function() {});
});


export default Router;


/*

    routes fetch models
    router maps urls
    model returns the JSON
    the controlle(last step before the template) r decorates it

*/