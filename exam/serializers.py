from .models import Question, Choice, Subject
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "subject", "question_text"]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            "id",
            "option1",
            "option2",
            "option3",
            "option4",
            "question",
            "Answer",
        ]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
