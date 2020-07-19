from django.shortcuts import render,redirect, get_object_or_404
from rest_framework.test import APIClient
from django.views.generic import ListView, DetailView, View, TemplateView
import json
# Create your views here.

def home(request):

    return render(request, 'home.html')

'''
def create(request):
    if request.method =='POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product=Product()
            product.title=request.POST['title']
            product.body=request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url=request.POST['url']
            else:
                product.url='http://'+request.POST['url']
            product.icon = request.FILES['icon']
            product.image=request.FILES['image']
            product.pub_date=timezone.datetime.now()
            
            product.hunter=request.user
            product.save()
            return redirect('/')
        else:
            return render(request,'products/create.html',{'error':'error here!'})
    else:
            return render(request,'products/create.html')
            '''



def test_predict_view(request):
    client = APIClient()
    if request.GET['age']:
        input_data = {
            "age": request.GET['age'],
            "workclass": 'Private',
            "fnlwgt": 34146,
            "education": "HS-grad",
            "education-num": 9,
            "marital-status": "Married-civ-spouse",
            "occupation": "Craft-repair",
            "relationship": "Husband",
            "race": "White",
            "sex": "Male",
            "capital-gain": 0,
            "capital-loss": 0,
            "hours-per-week": 68,
            "native-country": "United-States"
        }
        '''
        input_data = {
            "age": 37,
            "workclass": "Private",
            "fnlwgt": 34146,
            "education": "HS-grad",
            "education-num": 9,
            "marital-status": "Married-civ-spouse",
            "occupation": "Craft-repair",
            "relationship": "Husband",
            "race": "White",
            "sex": "Male",
            "capital-gain": 0,
            "capital-loss": 0,
            "hours-per-week": 68,
            "native-country": "United-States"
        }
        '''
        classifier_url = "/api/v1/income_classifier/predict"
        response = client.post(classifier_url, input_data, format='json')
        return render(request,'home.html',{'response':response})

