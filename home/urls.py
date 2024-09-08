
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('survey/take-survey/', views.takeSurvey, name='take-survey')
    # path('register/',views.goToRegister, name='register')
    
]