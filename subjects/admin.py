from django.contrib import admin

from.models import Subject, Activity

class ActivityInline(admin.StackedInline):
    model = Activity

class SubjectAdmin(admin.ModelAdmin):
    inlines = [ActivityInline,]

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Activity)