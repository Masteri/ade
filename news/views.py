from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from news.serializers import UserSerializer, GroupSerializer, NewsSerializer
from news.models import News
#from news.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from django.http import HttpResponse





@api_view()
def index(request):
    return render_to_response('news2/news.html', RequestContext(request))

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer



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
