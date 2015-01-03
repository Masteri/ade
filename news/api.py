from models import News
from serializers import NewsSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

class NLS(APIView):
    def get(self, request, format=None):
        news = News.objects.all()
        serialized_news = NewsSerializer(news, many=True)
        return Response(serialized_news.data)

class NLSDetal(APIView):
    def get_object(self, pk):
        try:
            return News.objects.get(pk=pk)
        except News.DoesNotExist:
            raise Http404



    def get(self, request, pk, format=None):
        news = self.get_object(pk)
        serialized_news = NewsSerializer(news)
        return Response(serialized_news.data)