import datetime

import pytz
from django.http import HttpResponse, JsonResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from languageprac.models import Vocabulary, Category, Record
from languageprac.serializers import VocabularySerializer, CategorySerializer


@api_view(['GET'])
def get_words_by_category(request, id):

    try:
        category = Category.objects.get(id=id)
        words = Vocabulary.objects.filter(category=id)
        serializer = VocabularySerializer(words, many=True)
        res = {
            'id': category.id,
            'name': category.name,
            'words': serializer.data
        }
        return JsonResponse(res, safe=False)
    except Vocabulary.DoesNotExist:
        return HttpResponse(status=404)

@api_view(['GET'])
def get_categories(request):
    try:
        categories = Category.objects.filter()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Category.DoesNotExist:
        return HttpResponse(status=404)



class RecordView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        a = [i for i in Record.objects.filter(user=request.auth.user_id).dates('pub_date', 'day')]
        return JsonResponse(a, safe=False)

