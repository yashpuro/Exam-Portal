from django.db import models
from django.http import HttpResponse

# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    semester = models.IntegerField()
    stream = models.CharField(max_length=200)

class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=0)
    question_text = models.CharField(max_length=200)
    

class Choice(models.Model):
    
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Answer = models.IntegerField()
