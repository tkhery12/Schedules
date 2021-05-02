from django.contrib import admin
from .models import Schedules,Enrolllist,Lecturer,examschedule
# Register your models here.
admin.site.register(Schedules)
admin.site.register(Enrolllist)
admin.site.register(Lecturer)
admin.site.register(examschedule)
