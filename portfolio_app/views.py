from django.shortcuts import render

def home(request):
    return render(request , 'home.html')

def project(request):
    return render(request , 'project.html')

def skill(request):
    return render(request , 'skill.html')
