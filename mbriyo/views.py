from django.utils.timezone import utc

__author__ = 'evangelie'
from django.shortcuts import render, redirect
import datetime

def WelcomePage(request):
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    return render(request, "mainPage.html",{"time": now})