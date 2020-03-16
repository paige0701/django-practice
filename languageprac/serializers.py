from rest_framework import serializers

from languageprac.models import Vocabulary, Category, Record


class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = ['id', 'eng', 'esp', 'kor']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['id', 'eng', 'kor', 'esp', 'user', 'modified_date', 'pub_date']