from django.shortcuts import render
from wordselector import views as wose

def createDjangoUser(req):
    pass

def login(req):
    
    return render(req,'users/login.html')


