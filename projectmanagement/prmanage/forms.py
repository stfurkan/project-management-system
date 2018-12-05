from django import forms
from .models import Task, Employee, EmployeeTask, Project, ProjectPM
from django.contrib.auth.models import User
from .middleware import get_current_user

class NewTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['subject','start_date','end_date','project']

class NewEmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['name']

class NewAssignEmployeeForm(forms.ModelForm):
    #task_id = forms.ModelChoiceField(queryset=Task.objects.filter(project__pk=project_id))
    class Meta:
        model = EmployeeTask
        fields = ['task_id','employee_id']


class NewProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name','description','start_date']

class NewAssignPmForm(forms.ModelForm):

    class Meta:
        model = ProjectPM
        fields = ['project_id','pm_id']
