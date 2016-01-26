from django import forms
import math
from .models import Subject, Activity, Log


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'color', 'priority']
        
    def clean_priority(self):
        priority = self.cleaned_data.get('priority')
        if priority < 1:
            raise forms.ValidationError("Priority must be a positive number")
        return math.fabs(priority) 
        
class LogForm(forms.Form):
    class Meta:
        model = Log
        fields = ['start_time', 'end_time', 'comment']
        
    def clean_end_time(self):
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        
        if start_time > end_time:
            raise forms.ValidationError("Start Time must come before End Time")
            
        return