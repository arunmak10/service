""" from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'severity', 'deadline', 'created_at')
    list_filter = ('priority', 'severity', 'created_at')

admin.site.register(Task, TaskAdmin) """

""" 
from django.contrib import admin
from .models import Task
from workers.models import Worker  # Adjust this import based on your app structure

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'severity', 'deadline', 'created_at')
    list_filter = ('priority', 'severity', 'created_at')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "assignee":
            # Exclude workers marked as not available
            kwargs["queryset"] = Worker.objects.filter(is_available=True)#.values('user')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Task, TaskAdmin) """

from django.contrib import admin
from django.db.models import Count
from .models import Task
from workers.models import Worker  # Adjust this import based on your app structure

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'severity', 'deadline', 'created_at')
    list_filter = ('priority', 'severity', 'created_at', 'completed_reason', 'completed_at')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "assignee":
            # Exclude workers marked as not available
            kwargs["queryset"] = Worker.objects.filter(is_available=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(num_completed=Count('completed_at'))

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        queryset = response.context_data['cl'].queryset
        # Get total number of created tasks
        total_created_tasks = queryset.count()
        # Get total number of completed tasks
        total_completed_tasks = queryset.filter(completed_at__isnull=False).count()

        # Update the context with the counts
        response.context_data['total_created_tasks'] = total_created_tasks
        response.context_data['total_completed_tasks'] = total_completed_tasks

        return response

admin.site.register(Task, TaskAdmin)


 