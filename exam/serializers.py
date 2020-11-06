from .models import Question , Choice , Subject  
from rest_framework import serializers 

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Question  
       fields = ['id', 'subject' , 'question_text']

         
class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Choice  
       fields = ['id', 'option1' , 'option2' , 'option3', 'option4','question','Answer']

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Subject 
       fields = ['id', 'subject_name' , 'semester' , 'stream']

         
         


