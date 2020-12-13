from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from todo_app.forms import TodoForm
from todo_app.models import Todo


def index(request):
    todos = Todo.objects.all().order_by('is_done', 'title')
    form = TodoForm()
    context = {
        'todos': todos,
        'form': form,
    }
    return render(request, 'index.html', context)


@require_POST
def create(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        todo = Todo(
            title=title,
            description=description)
        todo.save()
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'create_template.html', context)


def create_template(request, form=None, form_action='create', pk=None):
    if not form:
        form = TodoForm()
    context = {
        'form': form,
        'form_action': form_action,
        'pk': pk,
    }
    return render(request, 'create_template.html', context)


def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'GET':
        form = TodoForm(initial=todo.__dict__)
        return create_template(request, form, 'edit', pk=pk)
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            todo.title = form.cleaned_data['title']
            todo.description = form.cleaned_data['description']
            todo.save()
            return redirect(index)

        return create_template(
            request,
            form,
            form_action='edit',
            pk=pk
        )


@require_POST
def mark_todo_done(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect('index')


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('index')
