from django.conf.urls import  include
from . import views
from django.urls import path

urlpatterns = [
 path('test',views.test_predict_view, name = 'test'),
 
   
 
]