from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, DeleteView
from django.utils import timezone
from .forms import NewTaskForm, NewEmployeeForm, NewAssignEmployeeForm, NewProjectForm, NewAssignPmForm
from .models import Project, Task, Employee, EmployeeTask, ProjectPM

def home(request):
    projects = Project.objects.all()
    pms = ProjectPM.objects.all()
    return render(request, 'home.html', {'projects': projects, 'pms': pms})

def project_tasks(request, pk):
    project = get_object_or_404(Project, pk=pk)
    pms = ProjectPM.objects.filter(project_id=pk)
    return render(request, 'tasks.html', {'project': project, 'pms':pms})

@login_required
def new_task(request, pk):
    project = get_object_or_404(Project, pk=pk)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()

            return redirect('project_tasks', pk=project.pk)
    else:
        form = NewTaskForm()
    return render(request, 'new_task.html', {'project': project, 'form': form})

@login_required
def task_employees(request, pk, task_pk):
    task = EmployeeTask.objects.filter(task_id=task_pk)
    project = get_object_or_404(Project, pk=pk)
    employeex = Employee.objects.all()
    taskx = Task.objects.filter(pk=task_pk)
    #get_object_or_404(EmployeeTask, project__pk=pk, pk=task_pk)
    return render(request, 'task_employees.html', {'task': task, 'project': project, 'employeex': employeex, 'taskx': taskx})

def create_employee(request):
    if request.method == 'POST':
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()

            return redirect('home')
    else:
        form = NewEmployeeForm()
    return render(request, 'create_employee.html', {'form': form})

def list_employee(request):
    employees = Employee.objects.all()
    return render(request, 'employee.html', {'employees': employees})

def assign_employee(request):
    if request.method == 'POST':
        form = NewAssignEmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()

            return redirect('list_employee')
    else:
        form = NewAssignEmployeeForm()
    return render(request, 'assign_employee.html', {'form': form})

@login_required
def new_project(request):
    if request.method == 'POST':
        form = NewProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()

            return redirect('home')
    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {'form': form})

def assign_pm(request):
    if request.method == 'POST':
        form = NewAssignPmForm(request.POST)
        if form.is_valid():
            pm = form.save(commit=False)
            pm.save()

            return redirect('home')
    else:
        form = NewAssignPmForm()
    return render(request, 'assign_pm.html', {'form': form})


def save_employee_task(request):
    projects = Project.objects.all()
    pms = ProjectPM.objects.all()
    if request.method == 'POST':
        task_id = request.POST['task_id']
        print(task_id)
        employee_id = request.POST['employee_id']
        print(employee_id)
        emp_task = EmployeeTask.objects.create(task_id=Task.objects.get(subject=task_id), employee_id=Employee.objects.get(name=employee_id))


        return render(request, 'home.html', {'projects': projects, 'pms': pms})
    return render(request, 'home.html', {'projects': projects, 'pms': pms})


class TaskUpdateView(UpdateView):
    model = Task
    fields = ('subject', 'start_date', 'end_date', 'project',)
    template_name = 'edit_task.html'
    success_url = '/'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = '/'
