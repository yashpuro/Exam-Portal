from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Subject , Question , Choice
from django.template import loader
from .serializers import QuestionSerializer,AnswerSerializer,SubjectSerializer
# Create your views here.

def index(request):
    return HttpResponse("This is Exam Portal")

def admin(request):
    sub = Subject.objects.values('semester').distinct()
    ques = Question.objects.all()
    choice = Choice.objects.all() 
    context = {"subject":sub ,  "question":ques , "choice":choice}
    template = loader.get_template('exam/admin.html')
    return HttpResponse(template.render(context, request))
   


def SubjectViewSet(ModelViewSet, pk , stream):
    queryset = Subject.objects.filter(semester=pk , stream = stream).values()
    serializer_class =  SubjectSerializer(queryset, many=True)
    return JsonResponse(serializer_class.data, safe=False)  

def QuestionViewSet(ModelViewSet, pk ):
    queryset = Question.objects.filter(pk=pk)
    serializer_class =  QuestionSerializer(queryset, many=True)
    return JsonResponse(serializer_class.data, safe=False) 

def AnswerViewSet(ModelViewSet, pk ):
    queryset = Choice.objects.filter(question=pk)
    serializer_class =  AnswerSerializer(queryset, many=True)
    return JsonResponse(serializer_class.data, safe=False)     