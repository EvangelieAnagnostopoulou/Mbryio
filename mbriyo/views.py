from django.utils.timezone import utc
from mbriyo.models import Models
from forms import ModelForm, StationForm

__author__ = 'evangelie'
from django.shortcuts import render, redirect
import datetime

def WelcomePage(request):
    if request.method == 'GET':
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        form = ModelForm(initial={})
        return render(request, "mainPage.html",{"time": now, "form":form})
    if request.method == 'POST':
        station =request.POST.get('station')
        return render(request, "arrival.html",{"station":station})
