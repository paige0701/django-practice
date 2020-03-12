from django.http import HttpResponse, JsonResponse

# Create your views here.
from languageprac.models import Vocabulary
from languageprac.serializers import VocabularySerializer


def get_words_by_category(request, id):

    try:
        words = Vocabulary.objects.filter(category=id)
        serializer = VocabularySerializer(words, many=True)
        res = {
            'category': '',
            'words': serializer.data
        }
        return JsonResponse(res, safe=False)
    except Vocabulary.DoesNotExist:
        return HttpResponse(status=404)


