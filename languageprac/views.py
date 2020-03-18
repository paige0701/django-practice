import datetime
import json

from django.http import HttpResponse, JsonResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from languageprac.models import Vocabulary, Category, Record
from languageprac.serializers import VocabularySerializer, CategorySerializer, RecordSerializer
from polls.models import User


@api_view(['GET'])
def get_records_by_id(request, id):

    if '-' not in id:
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
    else:
        try:
            y,m,d = id.split('-')
            a = Record.objects.filter(user=request.auth.user_id, pub_date__startswith=datetime.date(int(y), int(m), int(d)))
            serializer = RecordSerializer(a, many=True)
            res = {
                'id': id,
                'name': id,
                'words': serializer.data
            }
            return JsonResponse(res, safe=False)
        except Record.DoesNotExist:
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

    def post(self, request):
        user = User.objects.get(id=request.auth.user_id)
        records = json.loads(request.data.get('records'))
        Record.objects.bulk_create([Record(eng=i['eng'], esp=i['esp'], kor=i['kor'], user=user) for i in records])
        return HttpResponse(status=200)