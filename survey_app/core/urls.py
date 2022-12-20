from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('survey/', SurveyView.as_view(), name='survey'),
    path('signup/', SignupView.as_view(), name='signup'),
    ]