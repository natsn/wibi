import DS from 'ember-data';

export default DS.Model.extend({
    recipient: DS.hasOne('user'), //ForeignKey(User,related_name='msg_recipient')
    sender: DS.hasOne('user'), //ForeignKey(User,related_name='msg_sender')
    text: DS.attr('string'),
    seen_by_recipient: DS.attr('boolean', {defaultValue:false})
});