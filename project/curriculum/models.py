from django.db import models
from django.contrib.auth.models import User
from utils.mixins import TranslatedModelMixin

class Level(models.Model, TranslatedModelMixin):
    title = models.CharField(max_length=255)
    es_title = models.CharField(max_length=255)
    position = models.IntegerField(default=1, help_text='What level/session is this?')
    language_code = 'en'
    translated_fields = ['title']
    class Meta:
        ordering = ('position',)

class Section(models.Model, TranslatedModelMixin):
    title = models.CharField(max_length=255)
    es_title = models.CharField(max_length=255)
    language_code = 'en'
    translated_fields = ['title']

class Page(models.Model, TranslatedModelMixin):
    level = models.ForeignKey(Level)
    section = models.ForeignKey(Section)
    title = models.CharField(max_length=255)
    html = models.TextField()
    display_welcome_video = models.BooleanField(default=False, help_text="By checking this the user will see their higher_up's welcome video if available.")
    es_title = models.CharField(max_length=255)
    es_html  = models.TextField()
    language_code = 'en'
    translated_fields = ['title', 'html']

class Edge(models.Model):
    u = models.ForeignKey(Page,related_name='from_page')
    v = models.ForeignKey(Page,related_name='to_page')

class Permission(models.Model):
    page = models.ForeignKey(Page)
    user = models.ForeignKey(User)

class Media(models.Model):
    file = models.FileField(upload_to = u'uploads/')

class Tip(models.Model, TranslatedModelMixin):
    text = models.CharField(max_length=255)
    es_text = models.CharField(max_length=255)
    language_code = 'en'
    translated_fields = ['text']

class CustomPage(models.Model, TranslatedModelMixin):
    html = models.TextField()
    es_html = models.TextField()
    language_code = 'en'
    translated_fields = ['html']

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

class Response(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    choices = models.CommaSeparatedIntegerField(max_length=255)
    free = models.TextField()
    attempt = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now=True)

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

# Home Visitor Curriculum:
# class HVLevel(Level):
#     pass
# class HVSection(Section):
#     pass
# class HVPage(Page):
#     level = models.ForeignKey(HVLevel,related_name='hv_level')
#     section = models.ForeignKey(HVSection,related_name='hv_section')
# class HVEdge(Edge):
#     u = models.ForeignKey(HVPage,related_name='hv_from_page')
#     v = models.ForeignKey(HVPage,related_name='hv_to_page')
# class HVPermission(Permission):
#     page = models.ForeignKey(HVPage)
# class HVTip(Tip):
#     pass
# class HVCustomPage(CustomPage):
#     pass
# class HVQuestion(Question):
#     page = models.ForeignKey(HVPage)
# class HVChoice(Choice):
#     question = models.ForeignKey(HVQuestion)
# class HVResponse(Response):
#     pass