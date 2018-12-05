from django.contrib import admin
from .models import Project, Task, Employee, EmployeeTask, ProjectPM

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Employee)
admin.site.register(EmployeeTask)
admin.site.register(ProjectPM)
