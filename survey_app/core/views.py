from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm

# Create your views here.


class HomePageView(View):
    def get(self, request):
        return render(request, 'index.html')

class SignupView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form' : form})

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

class SurveyView(View):
    def get(self, request):
        return render(request, 'survey.html')

    def post(self, request):
        return render(request, 'survey.html')
