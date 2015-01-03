from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.views.generic import TemplateView, ListView, DetailView

from rest_framework import generics, permissions
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import detail_route

from news.serializers import UserSerializer, GroupSerializer, NewsSerializer
from news.models import News
from news.permissions import *
from rest_framework import renderers, response
from rest_framework.decorators import api_view


class SnewsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return response(snippet.highlighted)

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)

news_list = SnewsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

class SimpleStaticView(TemplateView):
    def get_template_names(self):
        return [self.kwargs.get('template_name') + ".html"]

    def get(self, request, *args, **kwargs):
        from django.contrib.auth import authenticate, login
        if request.user.is_anonymous():
            #Auto-login the User for Demonstration Purposes
            user = authenticate()
            login(request, user)
        return super(SimpleStaticView, self).get(request, *args, **kwargs)






class NewsList(ListView):
    model = News
    #queryset = News.objects.get.all()
    #serializer_class = NewsSerializer



def index(request):
    return render_to_response('news.html', RequestContext(request))

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
