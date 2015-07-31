__author__ = 'evangelie'
from django import forms
from mbriyo.models import Models, Station



class ModelForm(forms.ModelForm):

    class Meta:
        model = Models
        error_css_class = 'error'

class StationForm(forms.ModelForm):

    class Meta:
        model = Station
        error_css_class = 'error'
