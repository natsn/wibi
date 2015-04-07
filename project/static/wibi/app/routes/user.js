import Ember from 'ember';

export default Ember.Route.extend({
  model: function(userID?){
    this.store.find('user', userID)
  }
});
