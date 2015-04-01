from django.db import models
from django.contrib.auth.models import User
import pytz

class Agency(models.Model):
    name = models.CharField(max_length=500)

class Profile(models.Model):
    user = models.OneToOneField(User)
    agency = models.ForeignKey(Agency)
    higher_up = models.ForeignKey('self', blank=True, null=True)
    LANGS = (
        ('en', 'English'),
        ('es', 'Spanish'),
    )
    language = models.CharField(max_length=2,choices=LANGS)

    TYPES = (
        ('P', 'Participant'),
        ('C', 'Coach'),
        ('T', 'Trainer/Consultant'),
    )
    type = models.CharField(max_length=1, choices=TYPES, default='P')
    coach_welcome_video = models.FileField(upload_to = u'coach_video/', max_length=255, null=True, blank=True)

    TIMEZONES = [(tz,tz) for tz in pytz.all_timezones]
    timezone = models.CharField(max_length=100, choices=TIMEZONES, default='US/Pacific')
    def is_with(self, profile):
        """
            This function determines if a user is associated with another user.
            It does this by examining the tree structure of Profile. For
            example, in the tree below... T is with C1, C1 is not with C2,
            T is with P3, C2 is not with P1, etc.

                 T
                / \___
               C1      \
               |        C2
               P1      /  \
                      P2   P3

            Usage:
                    P1.is_with(C1)
                    >>> True
                    P2.is_with(P3)
                    >>> False
                    P3.is_with(T)
                    >>> True
        """
        me = self
        you = profile

        hu = me.higher_up
        while hu is not None:
            if hu == you:
                return True
            else:
                hu = hu.higher_up
        hu = you.higher_up
        while hu is not None:
            if hu == me:
                return True
            else:
                hu = hu.higher_up

        return False

class Message(models.Model):
    recipient = models.ForeignKey(User,related_name='msg_recipient')
    sender = models.ForeignKey(User,related_name='msg_sender')
    text = models.TextField()
    seen_by_recipient = models.BooleanField(default=False)
    def __unicode__(self):
        return self.text

class Star(models.Model):
    value = models.IntegerField()
    recipient = models.ForeignKey(User,related_name='str_recipient')
    sender = models.ForeignKey(User,related_name='str_sender')

class PageVisit(models.Model):
    user = models.IntegerField(null=True)
    path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

class Error(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

class ClinicalNote(models.Model):
    pass