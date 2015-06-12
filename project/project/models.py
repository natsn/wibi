from django.contrib.auth.models import User
from django.db import models
from utils.mixins import TranslatedModelMixin, TitleMixin
import pytz

class Media(models.Model):
    file = models.FileField(upload_to = u'uploads/')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class VideoUpload(models.Model):
    user = models.ForeignKey(User)
    video = models.FileField(upload_to='video_uploads')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class VideoNote(models.Model):
    user = models.ForeignKey(User)
    video = models.ForeignKey(VideoUpload)
    mark = models.IntegerField()
    comment = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Agency(models.Model):
    name = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "Agencies"

class Profile(models.Model):
    user = models.OneToOneField(User)
    agency = models.ForeignKey(Agency)
    coach_welcome_video = models.FileField(upload_to = u'coach_welcome_videos/')
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

    def furthest_page_viewed(self, curriculum):
        # TODO Traverse linked list, compare to permissions
        my_perms = Permission.objects.filter(user=self)
        pages = Page.objects.filter(curriculum=curriculum)


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

class Message(models.Model):
    recipient = models.ForeignKey(User,related_name='msg_recipient')
    sender = models.ForeignKey(User,related_name='msg_sender')
    text = models.TextField()
    seen_by_recipient = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.text

class Star(models.Model):
    value = models.IntegerField()
    recipient = models.ForeignKey(User,related_name='str_recipient')
    sender = models.ForeignKey(User,related_name='str_sender')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class PageVisit(models.Model):
    user = models.ForeignKey(User)
    path = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Error(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    url = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class ClinicalNote(models.Model):
    coach = models.ForeignKey(User, related_name='cn_coach')
    participant = models.ForeignKey(User, related_name='cn_participant')
    note = models.TextField(help_text='This is a general note')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class ContactLog(models.Model):
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
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['date_and_time_of_contact']

class Curriculum(models.Model, TitleMixin):
    title = models.CharField(max_length=255)
    agency = models.ForeignKey(Agency)

class CurriculumAndProfile(models.Model):
    """
        This table distinguishes which profile's have access to which curriculum.
        A coach may have access to a home visitor training course and PALS. Participants
        will probably just have access to one curriculum (ePALS1 or ePALS2)
    """
    curriculum = models.ForeignKey(Curriculum)
    profile = models.ForeignKey(Profile)

class Level(models.Model, TranslatedModelMixin, TitleMixin):
    curriculum = models.ForeignKey(Curriculum)
    title = models.CharField(max_length=255)
    es_title = models.CharField(max_length=255)
    position = models.IntegerField(default=1, help_text='What level/session is this?')
    language_code = 'en'
    translated_fields = ['title']

    class Meta:
        ordering = ['position']

    @property
    def page_list(self):
        list = []
        curr = Page.objects.get(prv=None, level=self)
        while curr:
            list.append(curr)
            curr = curr.nxt
        return list

class Section(models.Model, TitleMixin):
    title = models.CharField(max_length=255)
    es_title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    language_code = 'en'
    translated_fields = ['title']

class Page(models.Model, TitleMixin):
    level = models.ForeignKey(Level)
    section = models.ForeignKey(Section,null=True)
    title = models.CharField(max_length=255)
    markdown = models.TextField()
    display_coach_welcome_video = models.BooleanField(default=False, help_text="By checking this the user will see their higher_up's welcome video if available.")
    es_title = models.CharField(max_length=255)
    es_markdown  = models.TextField()
    prv = models.ForeignKey('self',related_name='previous_page',null=True)
    nxt = models.ForeignKey('self',related_name='next_page',null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    language_code = 'en'
    translated_fields = ['title', 'markdown']



class Permission(models.Model):
    created = models.DateTimeField(auto_now_add=True)
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

    def __unicode__(self):
        return self.text

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

    def __unicode__(self):
        return self.text

class Response(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    choice_pks = models.CommaSeparatedIntegerField(max_length=255)
    text = models.TextField()
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

    def __unicode__(self):
        if self.text:
            return self.text
        else:
            return self.choice_pks