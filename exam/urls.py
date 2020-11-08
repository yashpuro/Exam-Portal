
from django.urls import include, path
from . import views
from exam.views import AnswerViewSet, QuestionViewSet, SubjectViewSet


urlpatterns = [
    path('', views.index , name = 'Home' ),
    path('admin', views.admin ,  name = 'admin'),
    path('subdetails/<int:pk>/<str:stream>' , SubjectViewSet.as_view , name= 'Subject Details'),
    path('quesdetails/<int:pk>' , QuestionViewSet.as_view() , name= 'Question Details'),
    path('ansdetails/<int:pk>' , AnswerViewSet.as_view() , name= 'Answer Details'),
    
]