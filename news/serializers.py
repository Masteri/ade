from rest_framework import serializers
from news.models import News
from django.contrib.auth.models import User, Group


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    #highlight = serializers.HyperlinkedIdentityField(view_name='NewsViewSet')
    class Meta:
        model = News
        fields = ('id', 'title', 'categoriya', 'image', 'images', 'autor', 'datapost', 'zmist')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')