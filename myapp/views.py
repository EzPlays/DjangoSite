from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    title = 'Django App!!'
    return render(request, 'index.html', {
        'title': title,
    })


def about(request):
    username = 'Ez'
    return render(request, 'about.html', {
        'username': username,
    })


def hello(request, username):
    print(username)
    return HttpResponse("<h1>hello %s</h1>" % username)


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects,
    })


def tasks(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks,
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            "form": CreateNewTask(),
        })
    else:
        Task.objects.create(
            title=request.POST['title'], descripcion=request.POST['descripcion'], project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject(),
        })
    else:
        Project.objects.create(
            name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    # project = Project.objects.get(id=id)
    tasks_p= Task.objects.filter(project_id = id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks_p,
    })

        # def projects(request):
        #     projects = list(Project.objects.values())
        #     return JsonResponse(projects, safe=False)

        # def tasks(request, id):
        #     # task = Task.objects.get(id=id)
        #     task = get_object_or_404(Task, id=id)
        #     return HttpResponse('task: %s ' % task.title)
