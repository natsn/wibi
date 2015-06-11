from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from project.models import Media, VideoUpload, VideoNote, Agency, Profile, Message, Star, PageVisit, Error, ClinicalNote, ContactLog, Curriculum, Level, Section, Page, Edge, Permission, Tip, CustomPage, Question, Choice, Response
from django.db import models

class MediaAdmin(admin.ModelAdmin):
    list_display = (u'id', 'file')
admin.site.register(Media, MediaAdmin)


class VideoUploadAdmin(admin.ModelAdmin):
    list_display = (u'id', 'user', 'video')
    list_filter = ('user',)
admin.site.register(VideoUpload, VideoUploadAdmin)


class VideoNoteAdmin(admin.ModelAdmin):
    list_display = (u'id', 'user', 'video', 'mark', 'comment')
    list_filter = ('user', 'video')
admin.site.register(VideoNote, VideoNoteAdmin)


class AgencyAdmin(admin.ModelAdmin):
    list_display = (u'id', 'name')
    search_fields = ('name',)
admin.site.register(Agency, AgencyAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'user',
        'agency',
        'media',
        'higher_up',
        'language',
        'type',
        'timezone',
    )
    list_filter = ('user', 'agency', 'media', 'higher_up')
admin.site.register(Profile, ProfileAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'recipient',
        'sender',
        'text',
        'seen_by_recipient',
    )
    list_filter = ('recipient', 'sender', 'seen_by_recipient')
admin.site.register(Message, MessageAdmin)


class StarAdmin(admin.ModelAdmin):
    list_display = (u'id', 'value', 'recipient', 'sender')
    list_filter = ('recipient', 'sender')
admin.site.register(Star, StarAdmin)


class PageVisitAdmin(admin.ModelAdmin):
    list_display = (u'id', 'user', 'path')
admin.site.register(PageVisit, PageVisitAdmin)


class ErrorAdmin(admin.ModelAdmin):
    list_display = (u'id', 'user', 'text', 'url')
    list_filter = ('user',)
admin.site.register(Error, ErrorAdmin)


class ClinicalNoteAdmin(admin.ModelAdmin):
    list_display = (u'id', 'coach', 'participant', 'note')
    list_filter = ('coach', 'participant')
admin.site.register(ClinicalNote, ClinicalNoteAdmin)


class ContactLogAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'coach',
        'participant',
        'date_and_time_of_contact',
        'type_of_contact',
    )
    list_filter = ('coach', 'participant', 'date_and_time_of_contact')
admin.site.register(ContactLog, ContactLogAdmin)


class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('title', u'id', 'agency', 'for_participant')
    list_filter = ('agency', 'for_participant')
admin.site.register(Curriculum, CurriculumAdmin)


class LevelAdmin(admin.ModelAdmin):
    list_display = ('title', u'id', 'curriculum', 'es_title', 'position')
    list_filter = ('curriculum',)
admin.site.register(Level, LevelAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', u'id', 'curriculum', 'es_title')
    list_filter = ('curriculum',)
admin.site.register(Section, SectionAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        u'id',
        'curriculum',
        'level',
        'section',
        'markdown',
        'display_welcome_video',
        'es_title',
        'es_markdown',
    )
    list_filter = ('curriculum', 'level', 'section', 'display_welcome_video')
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
admin.site.register(Page, PageAdmin)


class EdgeAdmin(admin.ModelAdmin):
    list_display = (u'id', 'u', 'v')
    list_filter = ('u', 'v')
admin.site.register(Edge, EdgeAdmin)


class PermissionAdmin(admin.ModelAdmin):
    list_display = (u'id', 'page', 'user')
    list_filter = ('page', 'user')
admin.site.register(Permission, PermissionAdmin)


class TipAdmin(admin.ModelAdmin):
    list_display = (u'id', 'curriculum', 'text', 'es_text')
    list_filter = ('curriculum',)
admin.site.register(Tip, TipAdmin)


class CustomPageAdmin(admin.ModelAdmin):
    list_display = (u'id', 'markdown', 'es_markdown')
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
admin.site.register(CustomPage, CustomPageAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'page',
        'text',
        'type',
        'is_scoreable',
        'position',
        'es_text',
    )
    list_filter = ('page', 'is_scoreable')
admin.site.register(Question, QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'question',
        'text',
        'feedback',
        'correct',
        'position',
        'es_text',
        'es_feedback',
    )
    list_filter = ('question', 'correct')
admin.site.register(Choice, ChoiceAdmin)


class ResponseAdmin(admin.ModelAdmin):
    list_display = (u'id', 'user', 'question', 'choices', 'free', 'attempt')
    list_filter = ('user', 'question')
admin.site.register(Response, ResponseAdmin)