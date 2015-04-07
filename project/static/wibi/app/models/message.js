import DS from 'ember-data';

export default DS.Model.extend({
    recipient: DS.hasOne('user'), //models.ForeignKey(User,related_name='msg_recipient')
    sender: DS.hasOne('user'), //models.ForeignKey(User,related_name='msg_sender')
    text: DS.attr('string'), //models.TextField()
    seen_by_recipient: DS.attr('boolean', {defaultValue:false}) //models.BooleanField(default=False)
});