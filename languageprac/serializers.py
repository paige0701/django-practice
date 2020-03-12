from rest_framework import serializers

from languageprac.models import Vocabulary


class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = ['id', 'eng', 'esp', 'kor', 'category']