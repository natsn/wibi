from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from project.serializers import *
from django.http import HttpResponse
from project.models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class LevelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows level to be viewed or edited.
    """
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class VideoNoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows note to be viewed or edited.
    """
    queryset = VideoNote.objects.all()
    serializer_class = VideoNoteSerializer

class ErrorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows error to be viewed or edited.
    """
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer

class StarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows star to be viewed or edited.
    """
    queryset = Star.objects.all()
    serializer_class = StarSerializer

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows message to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class PageVisitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pagevisit to be viewed or edited.
    """
    queryset = PageVisit.objects.all()
    serializer_class = PageVisitSerializer

class AgencyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows agency to be viewed or edited.
    """
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profile to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class SectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows section to be viewed or edited.
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows page to be viewed or edited.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows permission to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class MediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows media to be viewed or edited.
    """
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class TipViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tip to be viewed or edited.
    """
    queryset = Tip.objects.all()
    serializer_class = TipSerializer

class CustomPageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows custompage to be viewed or edited.
    """
    queryset = CustomPage.objects.all()
    serializer_class = CustomPageSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows question to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows choice to be viewed or edited.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ResponseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows response to be viewed or edited.
    """
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

def home(request):
    return render_to_response('index.html', RequestContext(request))
