import DS from 'ember-data';

export default DS.Model.extend({
  // last_login: DS.attr('date')
  // is_superuser: DS.attr('boolean'),
  // first_name: DS.attr('string'),
  // last_name: DS.attr('string'),
  // is_staff: DS.attr('boolean'),
  // is_active: DS.attr('boolean')
  // date_joined: DS.attr('date'),
  username: DS.attr('string'),
  email: DS.attr('string')
});

/*
  PRIMARY KEY: id
  UNIQUE KEY: username
*/

// class Profile(models.Model):
//     user = models.OneToOneField(User)
//     agency = models.ForeignKey(Agency)
//     higher_up = models.ForeignKey('self', blank=True, null=True)
//     LANGS = (
//         ('en', 'English'),
//         ('es', 'Spanish'),
//     )
//     language = models.CharField(max_length=2,choices=LANGS)

//     TYPES = (
//         ('P', 'Participant'),
//         ('C', 'Coach'),
//         ('T', 'Trainer/Consultant'),
//     )
//     type = models.CharField(max_length=1, choices=TYPES, default='P')
//     coach_welcome_video = models.FileField(upload_to = u'coach_video/', max_length=255, null=True, blank=True)

//     TIMEZONES = [(tz,tz) for tz in pytz.all_timezones]
//     timezone = models.CharField(max_length=100, choices=TIMEZONES, default='US/Pacific')

