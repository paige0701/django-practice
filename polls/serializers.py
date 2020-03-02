from rest_framework import serializers

from polls.models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    question_text = serializers.SerializerMethodField()
    class Meta:
        model = Choice
        fields = ['id', 'question_text', 'choice_text', 'votes']

    # custom field manipulation
    def get_question_text(self, obj):
        return obj.question.question_text

    def update(self, instance, validated_data):
        instance.votes=validated_data.get('choice', instance.votes)
        instance.save()
        return instance

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date']

    # def create(self, validated_data):
    #     return Question.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.question_text = validated_data.get('question_text', instance.question_text)
    #     instance.pub_date=validated_data.get('pub_date', instance.pub_date)
    #     instance.save()
    #     return instance