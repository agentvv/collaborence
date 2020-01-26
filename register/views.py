from django.shortcuts import render

def index(response):
    return render(response, 'register/base.html')