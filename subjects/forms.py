from django import forms
import math
from .models import Subject, Activity, Log
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'color', 'priority']
        
    def clean_priority(self):
        priority = self.cleaned_data.get('priority')
        if priority < 1:
            raise forms.ValidationError("Priority must be a positive number")
        return math.fabs(priority) 
        
class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        exclude = ('activity',)
        
    def __init__(self, *args, **kwargs):
        super(LogForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add Log Entry'))
        
        def clean_end_time(self):
            start_time = self.cleaned_data.get('start_time')
            end_time = self.cleaned_data.get('end_time')
            
            if start_time > end_time:
                raise forms.ValidationError("Start Time must come before End Time")
                
            return