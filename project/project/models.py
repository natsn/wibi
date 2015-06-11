from django.contrib.auth.models import User
from django.db import models
from utils.mixins import TranslatedModelMixin
import pytz

# Field Mixins

class TrackingFieldsMixin():
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

# General Models

class Media(models.Model, TrackingFieldsMixin):
    file = models.FileField(upload_to = u'uploads/')

class VideoUpload(models.Model, TrackingFieldsMixin):
    user = models.ForeignKey(User)
    video = models.FileField(upload_to='video_uploads')

class VideoNote(models.Model, TrackingFieldsMixin):
    user = models.ForeignKey(User)
    video = models.ForeignKey(VideoUpload)
    mark = models.IntegerField()
    comment = models.CharField(max_length=255)

class Agency(models.Model, TrackingFieldsMixin):
    name = models.CharField(max_length=500)
    class Meta:
        verbose_name_plural = "Agencies"

class Profile(models.Model):
    user = models.OneToOneField(User)
    agency = models.ForeignKey(Agency)
    media = models.ForeignKey(Media, help_text="Upload Coach Welcome Video as media, then link it here.")
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
    TIMEZONES = [(tz,tz) for tz in pytz.all_timezones]
    timezone = models.CharField(max_length=100, choices=TIMEZONES, default='US/Pacific')
    def belongs_to(self, profile):
        """
            This function determines if a user is associated with another user.
            It does this by examining the tree structure of Profile. For
            example, in the tree below... T is with C1, C1 is not with C2,
            T is with P3, C2 is not with P1, etc.

                 T
                / \____
               C1      \
               |        C2
               P1      /  \
                      P2   P3

            Usage:
                    P1.belongs_to(C1)
                    >>> True
                    P2.belongs_to(P3)
                    >>> False
                    P3.belongs_to(T)
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

class Message(models.Model, TrackingFieldsMixin):
    recipient = models.ForeignKey(User,related_name='msg_recipient')
    sender = models.ForeignKey(User,related_name='msg_sender')
    text = models.TextField()
    seen_by_recipient = models.BooleanField(default=False)
    def __unicode__(self):
        return self.text

class Star(models.Model, TrackingFieldsMixin):
    value = models.IntegerField()
    recipient = models.ForeignKey(User,related_name='str_recipient')
    sender = models.ForeignKey(User,related_name='str_sender')

class PageVisit(models.Model, TrackingFieldsMixin):
    user = models.IntegerField(null=True)
    path = models.CharField(max_length=255)

class Error(models.Model, TrackingFieldsMixin):
    user = models.ForeignKey(User)
    text = models.TextField()
    url = models.CharField(max_length=255)

class ClinicalNote(models.Model, TrackingFieldsMixin):
    coach = models.ForeignKey(User, related_name='cn_coach')
    participant = models.ForeignKey(User, related_name='cn_participant')
    note = models.TextField(help_text='This is a general note')

class ContactLog(models.Model, TrackingFieldsMixin):
    coach = models.ForeignKey(User, related_name='cl_coach')
    participant = models.ForeignKey(User, related_name='cl_participant')
    date_and_time_of_contact = models.DateTimeField(verbose_name="Date and time of contact, (Y-m-d H:M)")
    CONTACT_TYPES = (
        (0, "Phone call"),
        (1, "Video call"),
        (2, "Text"),
        (3, "Email"),
        (4, "Private message in program"),
        (5, "Home visit"),
        (6, "Face to face (outside home visit)"),
        (7, "Other"),
    )
    type_of_contact = models.IntegerField(max_length=1,default=7,choices=CONTACT_TYPES,verbose_name='How were they contacted?')

    class Meta:
        ordering = ['date_and_time_of_contact']

class Curriculum(models.Model):
    title = models.CharField(max_length=255)
    agency = models.ForeignKey(Agency)
    for_participant = models.BooleanField(default=False, help_text='Viewable by the participant.')

class Level(models.Model, TranslatedModelMixin):
    curriculum = models.ForeignKey(Curriculum)
    title = models.CharField(max_length=255)
    es_title = models.CharField(max_length=255)
    position = models.IntegerField(default=1, help_text='What level/session is this?')
    language_code = 'en'
    translated_fields = ['title']
    class Meta:
        ordering = ('position',)

    def __str__(self):
        return self.title

class Section(models.Model, TranslatedModelMixin):
    curriculum = models.ForeignKey(Curriculum)
    title = models.CharField(max_length=255)
    es_title = models.CharField(max_length=255)
    language_code = 'en'
    translated_fields = ['title']

class Page(models.Model, TranslatedModelMixin):
    curriculum = models.ForeignKey(Curriculum)
    level = models.ForeignKey(Level)
    section = models.ForeignKey(Section)
    title = models.CharField(max_length=255)
    markdown = models.TextField()
    display_welcome_video = models.BooleanField(default=False, help_text="By checking this the user will see their higher_up's welcome video if available.")
    es_title = models.CharField(max_length=255)
    es_markdown  = models.TextField()
    language_code = 'en'
    translated_fields = ['title', 'markdown']

class Edge(models.Model):
    u = models.ForeignKey(Page,related_name='from_page')
    v = models.ForeignKey(Page,related_name='to_page')

class Permission(models.Model, TrackingFieldsMixin):
    page = models.ForeignKey(Page)
    user = models.ForeignKey(User)

class Tip(models.Model, TranslatedModelMixin):
    curriculum = models.ForeignKey(Curriculum)
    text = models.CharField(max_length=255)
    es_text = models.CharField(max_length=255)
    language_code = 'en'
    translated_fields = ['text']

class CustomPage(models.Model, TranslatedModelMixin):
    markdown = models.TextField()
    es_markdown = models.TextField()
    language_code = 'en'
    translated_fields = ['markdown']

class Question(models.Model, TranslatedModelMixin):
    page = models.ForeignKey(Page)
    text = models.CharField(max_length=1000,blank=False)
    TYPES = (
        ('ra', 'radio'),
        ('ch', 'checkbox'),
        ('tx', 'text'),
    )
    type = models.CharField(max_length=2,choices=TYPES)
    is_scoreable = models.BooleanField(default=True,help_text="Will the answer to this question be scored?")
    position = models.IntegerField()

    es_text = models.CharField(max_length=1000,blank=False)
    language_code = 'en'
    translated_fields = ['text']
    class Meta:
        ordering = ['position']

class Choice(models.Model, TranslatedModelMixin):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=1000,blank=False)
    feedback = models.CharField(max_length=1000,blank=True)
    correct = models.BooleanField(blank=False,default=False,help_text="Is this a correct answer?")
    position = models.IntegerField()

    es_text = models.CharField(max_length=1000,blank=False)
    es_feedback = models.CharField(max_length=1000,blank=True)
    language_code = 'en'
    translated_fields = ['text']
    class Meta:
        ordering = ['position']

class Response(models.Model, TrackingFieldsMixin):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    choices = models.CommaSeparatedIntegerField(max_length=255)
    free = models.TextField()
    attempt = models.IntegerField(default=1)

    @property
    def selected(self):
        if len(self.choices > 0):
            choice_pks = self.choices.split(',')
            choices = Choice.objects.filter(pk__in=choice_pks.split(','))
            return choices
        else:
            return None

    @property
    def correct(self):
        all_correct = False
        correct_answers = Choice.objects.filter(question=self.question, correct=True)
        if list(self.selected) == list(correct_answers):
            all_correct = True
        return all_correct