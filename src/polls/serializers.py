from rest_framework import serializers
from . import models


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Choice
        fields = (
            'id',
            'choice_text',
            'votes',
        )


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    total_votes = serializers.SerializerMethodField()

    def create(self, validated_data):
        choice_validated_data = validated_data.pop('choices')
        question = models.Question.objects.create(**validated_data)
        choice_set_serializer = self.fields['choices']
        for each in choice_validated_data:
            each['question'] = question
        choices = choice_set_serializer.create(choice_validated_data)
        return question

    class Meta:
        model = models.Question
        fields = (
            'id',
            'question_text',
            'pub_date',
            'choices',
            'total_votes',
        )

    def get_total_votes(self, obj):
        return getattr(obj, 'total_votes', 0)
