from django.contrib import admin

# Register your models here.

from . import models

class TaskAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'task', 'completed', 'created_at')

admin.site.register(models.Task, TaskAdmin)