from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime, timedelta
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    def get_task_count(self):
        return Task.objects.filter(project=self).count()
    def get_active_task_count(self):
        return Task.objects.filter(project=self, end_date__gte=timezone.now()).count()



class Task(models.Model):
    subject = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now()+timedelta(days=1))
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

    def get_employee_status(self):
        employee_id = EmployeeTask.objects.filter(task_id=self).values('employee_id')
        return employee_status_count
        #, start_date__lte=timezone.now(), end_date__gte=timezone.now()



class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class EmployeeTask(models.Model):
    task_id = models.ForeignKey(Task, related_name='employeetasks', on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, related_name='employeetasks', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('task_id', 'employee_id',)



class ProjectPM(models.Model):
    project_id = models.ForeignKey(Project, related_name='projectpms', on_delete=models.CASCADE)
    pm_id = models.ForeignKey(User, related_name='projectpms', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_id)
