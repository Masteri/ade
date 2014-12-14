from django.forms import widgets
from rest_framework import serializers
from news.models import News
from django.contrib.auth.models import User, Group

class SnippetSerializer(serializers.Serializer):
    def create(self, validated_data):
            """
            http://www.django-rest-framework.org/tutorial/1-serialization/#introduction
            Create and return a new `Snippet` instance, given the validated data.
            """
            return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
            """
            Update and return an existing `Snippet` instance, given the validated data.
            """
            instance.title = validated_data.get('title', instance.title)
            """
            instance.code = validated_data.get('code', instance.code)
            instance.linenos = validated_data.get('linenos', instance.linenos)
            instance.language = validated_data.get('language', instance.language)
            instance.style = validated_data.get('style', instance.style)
            """
            instance.save()
            return instance

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


