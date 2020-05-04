import datetime
import json

from django.db.models import Q
from django.http import HttpResponse, JsonResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from languageprac.models import Vocabulary, Category, Record, FavouriteVocabulary
from languageprac.pagination import get_pagination_result, \
    get_pagination_class
from languageprac.serializers import VocabularySerializer, CategorySerializer, RecordSerializer
from languageprac.utils import get_request_params
from polls.models import User


@api_view(['GET'])
def get_word_of_the_day(request):
    user_id = request.user.id
    record = Record.objects.filter(user_id=user_id).order_by('?').first()
    serializer = RecordSerializer(record)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_records_by_id(request, id):

    if '-' not in id:
        try:

            category = Category.objects.get(id=id)

            params = get_request_params(request.query_params)
            page_size = params['page_size']

            if 'search' in request.query_params:
                search = request.query_params['search']
                words = Vocabulary.objects.filter(category=id).filter(Q(eng__contains=search) |
                                                                      Q(kor__contains=search) |
                                                                      Q(esp__contains=search))
            else:
                words = Vocabulary.objects.filter(category=id)

            # paging
            paginator = get_pagination_class(page_size)

            context = paginator.paginate_queryset(words, request)

            # serialize paginated list
            serializer = VocabularySerializer(context, many=True)

            res = {
                'id': category.id,
                'name': category.name,
                'count': words.count(),
                'page': paginator.page.number,
                'words': serializer.data
            }

            return JsonResponse(res, safe=False)
        except Vocabulary.DoesNotExist:
            return HttpResponse(status=404)
    else:
        try:
            y, m, d = id.split('-')

            params = get_request_params(request.query_params)
            page_size = params['page_size']

            records = Record.objects.filter(user=request.auth.user_id,
                                            pub_date__startswith=datetime.date(int(y), int(m), int(d)))

            # paging
            paginator = get_pagination_class(page_size)

            context = paginator.paginate_queryset(records, request)

            serializer = RecordSerializer(context, many=True)

            res = {
                'id': id,
                'name': id,
                'count': records.count(),
                'page': paginator.page.number,
                'words': serializer.data
            }
            return JsonResponse(res, safe=False)
        except Record.DoesNotExist:
            return HttpResponse(status=404)


@api_view(['GET'])
def get_categories(request):
    try:

        page_size = 20
        if 'page_size' in request.query_params:
            page_size = request.query_params['page_size']

        if 'search_text' in request.query_params:
            search = request.query_params['search_text']
            categories = Category.objects.filter(Q(name__icontains=search)).order_by('-pub_date')
        else:
            categories = Category.objects.filter().order_by('-pub_date')

        paginator = get_pagination_class(page_size)

        context = paginator.paginate_queryset(categories, request)

        paging = get_pagination_result(paginator, categories.count())

        serializer = CategorySerializer(context, many=True)

        res = {
            'page': paging,
            'data': serializer.data
        }

        return JsonResponse(res, safe=False)
    except Category.DoesNotExist:
        return HttpResponse(status=404)


class RecordView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        a = [i for i in Record.objects.filter(user=request.auth.user_id).dates('pub_date', 'day')]
        return JsonResponse(a, safe=False)

    def post(self, request):
        user = User.objects.get(id=request.auth.user_id)
        records = json.dumps(request.data.get('records'))
        records = json.loads(records)  # todo : whats the point of this?
        Record.objects.bulk_create([Record(eng=i['eng'], esp=i['esp'], kor=i['kor'], user=user) for i in records])
        return HttpResponse(status=200)


class FavouriteCategoryView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user_id = request.auth.user_id
        vocab_id = request.data.get('vocab_id')

        # delete
        if 'id' in request.data:
            id = request.data.get('id')
            try:
                # delete favourite
                FavouriteVocabulary.objects.filter(id=id).delete()
                return HttpResponse(status=200)
            except IOError:
                return HttpResponse(status=400)

        else:

            fav = FavouriteVocabulary.objects.create(user_id=user_id, category_vocab_id=vocab_id)
            if fav:
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=400)

