from django.shortcuts import render

# Create your views here.
def task_list(request):
    context = {}
    return render(request, 'task_list.html', context)

def task_update(request):
    context = {}
    return render(request, 'task_update.html', context)

def task_delete(request):
    context = {}
    return render(request, 'task_delete.html', context)

