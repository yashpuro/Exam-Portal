
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name = 'Home' ),
    path('admin', views.admin ,  name = 'admin'),
    path('subdetails/<int:pk>/<str:stream>' , views.SubjectViewSet , name= 'Subject Details'),
    path('quesdetails/<int:pk>' , views.QuestionViewSet , name= 'Question Details'),
    path('ansdetails/<int:pk>' , views.AnswerViewSet , name= 'Answer Details')
]