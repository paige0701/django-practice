from rest_framework import serializers

from polls.models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"