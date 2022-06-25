from django.contrib import admin
from .models import notifications, profile, course_shedule, quiz_assignment, MESSAGE

# Register your models here.
admin.site.register(profile)
admin.site.register(notifications)
admin.site.register(course_shedule)
admin.site.register(quiz_assignment)
admin.site.register(MESSAGE)