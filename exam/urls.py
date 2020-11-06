
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name = 'Home' ),
    path('admin', views.admin ,  name = 'admin'),
    path('subdetails/<int:pk>' , views.SubjectViewSet , name= 'subject details')
]
