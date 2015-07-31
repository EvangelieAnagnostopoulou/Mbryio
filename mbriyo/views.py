__author__ = 'evangelie'
from django.shortcuts import render, redirect

def WelcomePage(request):
    return render(request, "mainPage.html")