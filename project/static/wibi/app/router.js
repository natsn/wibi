import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.route('message', function() {});
  this.route('user', function() {});
});


export default Router;


/*

    routes fetch models
    router maps urls
    model returns the JSON
    the controller (last step before the template) and decorates it

*/