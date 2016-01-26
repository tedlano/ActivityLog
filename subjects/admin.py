from django.contrib import admin
from.models import Subject, Activity, Log

class ActivityInline(admin.StackedInline):
    model = Activity

class SubjectAdmin(admin.ModelAdmin):
    inlines = [ActivityInline,]
    
class LogInline(admin.StackedInline):
    model = Log
    
class ActivityAdmin(admin.ModelAdmin):
    inlines = [LogInline,]

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Log)