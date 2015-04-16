from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from project.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse 
from project.models import Tip

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

def home(request):
    return render(request,'index.html')

def tip(request, id):
    tipOutput  = Tip.objects.filter(id=id)
    if len(tipOutput) != 0:
        jsonOutput = '{"id": %d, "text": "%s", "es_text": "%s"}' %(tipOutput[0].id, tipOutput[0].text, tipOutput[0].es_text)
        return HttpResponse(jsonOutput)
    else:
        errorOutput = '{}'
        return HttpResponse(errorOutput)
