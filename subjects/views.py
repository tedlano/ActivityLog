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
    activity = get_object_or_404(Activity, subject_id=subject_pk, pk=activity_pk)
    form = LogForm(request.POST or None)
    
    try:
        logs = Log.objects.filter(activity_id=activity_pk)
        
        for log in logs:
            log.start_time = log.start_time.strftime("%Y-%m-%d %H:%M")
            log.end_time = log.end_time.strftime("%Y-%m-%d %H:%M")
            
    except Log.DoesNotExist:
        logs = None

    if form.is_valid():
        form.save()
        # instance = form.save(commit=False)
        # instance.save()
        form = None
    
    
    # try:
    #     logs_temp = Log.objects.get(activity_id=activity_pk)
    #     logs = []
        
    #     for log in logs_temp:
    #         log_date = log.start_time.strftime("%Y-%m-%d")
    #         log_comment = log.comment
    #         log_duration = "-"
            
    #         if log.end_time is not None:
    #             d
                
            
    #         log.append({'date': log.
            
            
    # except Log.DoesNotExist:
    #     logs = None
    
    context = {
        'activity': activity,
        'logs': logs,
        'form': form
    }
    
    return render(request, 'subjects/activity_detail.html', context)