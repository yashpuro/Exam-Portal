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


def SubjectViewSet(ModelViewSet, pk):
    queryset = Subject.objects.filter(semester=pk).values()
    serializer_class =  SubjectSerializer(queryset, many=True)
    #permisssion_classes = [permissions.IsAuthenticated] 
    return JsonResponse(serializer_class.data, safe=False)    
