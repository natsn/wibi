from django.contrib.auth.models import User, Group
from rest_framework import serializers
from project.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class LevelSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Level
 		fields = ('title', 'es_title', 'position')

class NoteSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Note
 		fields = ('user', 'video', 'mark', 'comment')

class ErrorSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Error
 		fields = ('user', 'text', 'created')

class StarSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Star
 		fields = ('value', 'recipient', 'sender')

class MessageSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Message
 		fields = ('recipient', 'sender', 'text', 'seen_by_recipient')

class PageVisitSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = PageVisit
 		fields = ('user', 'path', 'created_at')

class AgencySerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Agency
 		fields = ('name')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Profile
 		fields = ('user', 'agency', 'higher_up', 'language', 'type', 'coach_welcome_video', 'timezone')

class SectionSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Section
 		fields = ('title', 'es_title')

class PageSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Page
 		fields = ('level', 'section', 'title', 'html', 'display_welcome_video', 'es_title', 'es_html')

class EdgeSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Edge
 		fields = ('u', 'v')

class PermissionSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Permission
 		fields = ('page', 'user')

class MediaSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Media
 		fields = ('file')

class TipSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Tip
 		fields = ('text', 'es_text')

class CustomPageSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = CustomPage
 		fields = ('html', 'es_html')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Question
 		fields = ('page', 'text', 'type', 'is_scoreable', 'position', 'es_text')

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Choice
 		fields = ('question', 'text', 'feedback', 'correct', 'position', 'es_text', 'es_feedback')

class ResponseSerializer(serializers.HyperlinkedModelSerializer):
 	class Meta:
 		model = Response
 		fields = ('user', 'question', 'choices', 'free', 'attempt', 'created')