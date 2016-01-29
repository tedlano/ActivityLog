from django.shortcuts import render, get_object_or_404 
from .models import Subject, Activity, Log
from .forms import LogForm

def subject_list(request):   
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects
    }
    
    return render(request, 'subjects/subject_list.html', context)

def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    context = {
        'subject': subject
    }
    return render(request,  'subjects/subject_detail.html', context)


def activity_detail(request, subject_pk, activity_pk):
    
    # Get all Log entries for given activity
    def getLogs(activity_pk):
        try:
            logs = Log.objects.filter(activity_id=activity_pk)
            
            # Change display of datetime variables
            for log in logs:
                log.created_at = log.created_at.strftime("%Y-%m-%d %H:%M")
                hours = log.duration // 60
                minutes = log.duration % 60
                log.duration = "%d:%02d" % (hours, minutes)
            
        except Log.DoesNotExist:
            logs = None
            
        return logs
    
    # Get activity from DB, Form object, and Log entries
    activity = get_object_or_404(Activity, subject_id=subject_pk, pk=activity_pk)
    logs = getLogs(activity_pk)
    
    # Validate form
    if request.method == "POST":
        data = request.POST
        hours = int(data['hour'])
        minutes = int(data['min'])
        seconds = int(data['sec'])
        
        if seconds >= 30:
            minutes = minutes + 1
            
        dur = hours * 60 + minutes

        logObj = Log(comment=data['comment'], duration=dur, activity=activity)
        logObj.save()
        logs = getLogs(activity_pk)
        
    context = {
        'activity': activity,
        'logs': logs,
    }
    
    return render(request, 'subjects/activity_detail.html', context)