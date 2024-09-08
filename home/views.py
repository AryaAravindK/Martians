from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'home.html')

def takeSurvey(request):
    if request.method == 'POST':
        return HttpResponse('post method')
    else:
        return render(request,'survey.html')

