from django import forms
from .models import Meetings
 
from django import forms


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meetings
        fields = ['topic','duration', 'starttime','passwords',]
        #For Label tag
