from django import forms
import math
from .models import Subject, Activity, Log
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.translation import ugettext_lazy as _


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'color', 'priority']
        
    def clean_priority(self):
        priority = self.cleaned_data.get('priority')
        if priority < 1:
            raise forms.ValidationError("Priority must be a positive number")
        return math.fabs(priority) 
        
# http://stackoverflow.com/questions/16356289/how-to-show-datepicker-calender-on-datefield   
# https://www.reddit.com/r/django/comments/2abs90/how_can_i_use_a_datepicker_in_a_crispy_form/
# class LogForm(forms.Form):
#     start_time = forms.CharField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
#     duration = forms.TextInput(
#     comment = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
    
    
class LogForm(forms.ModelForm):
#     duration = forms.IntegerField(required=True)
    
    class Meta:
        model = Log
        fields = ('duration', 'comment')
#         labels = {
#             'duration': _('Duration (Minutes)')
#         }
#         widgets = {
#             'start_time': forms.DateInput(attrs={'class':'datepicker'}) 
#         }
        
#     def __init__(self, *args, **kwargs):
#         super(LogForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Add Log Entry'))
        
       