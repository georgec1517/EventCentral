from django import forms
from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields= ('name', 'event_date','opentodept', 'description','event_image',)
        labels = {
            'name' : '',
            'event_date' : '',
            'opentodept' : 'Open to Department',
            'description' : '',
            'event_image' : 'Add Display Image (Not Required) ',
            
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Event Title'}),
            'event_date' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Date'}),
            'description' : forms.Textarea(attrs={'class':'form-control','placeholder': 'Description'}),
            'opentodept' : forms.Select(attrs={'class':"form-select",})
        }