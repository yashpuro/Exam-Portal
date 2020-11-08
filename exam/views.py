from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .models import Subject, Question, Choice
from django.template import loader
from .serializers import QuestionSerializer, AnswerSerializer, SubjectSerializer
from django.views import View



def index(request):
    return HttpResponse("This is Exam Portal")


def admin(request):
    sub = Subject.objects.values('semester').distinct()
    ques = Question.objects.all()
    choice = Choice.objects.all()
    context = {"subject": sub, "question": ques, "choice": choice}
    template = loader.get_template('exam/admin.html')
    return HttpResponse(template.render(context, request))


class SubjectViewSet(View):
    def get(self, pk, stream):
        queryset = Subject.objects.filter(semester=pk, stream=stream).values()
        serializer_class = SubjectSerializer(queryset, many=True)
        return HttpResponse(serializer_class.data)


class QuestionViewSet(View):
    def get(self, pk):
        queryset = Question.objects.filter(pk=pk)
        serializer_class = QuestionSerializer(queryset, many=True)
        return HttpResponse(serializer_class.data)


class AnswerViewSet(View):
    def get(self, pk):
        queryset = Choice.objects.filter(question=pk)
        serializer_class = AnswerSerializer(queryset, many=True)
        return HttpResponse(serializer_class.data)
