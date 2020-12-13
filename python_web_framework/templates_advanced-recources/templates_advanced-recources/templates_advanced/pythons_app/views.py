from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PythonCreateForm, RegisterForm, LoginForm, ProfileForm
from .models import Python


def index(req):
    pythons = Python.objects.all()
    for python in pythons:
        python.can_delete = python.created_by.id == req.user.id
    context = {
        'pythons': pythons,
        'current_page': 'home'
    }
    return render(req, 'index.html', context)


@login_required
def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
        return render(req, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(data=req.POST, files=req.FILES)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')


def python_details(request, pk, slug=None):
    python = Python.objects.get(pk=pk)
    if slug and python.name.lower() != slug.lower():
        return HttpResponse('404')
    context = {
        'python': python,
    }
    return render(request, 'python.html', context)


def register_user(request):
    if request.method == 'GET':
        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, 'register.html', context)
    else:
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return_url = get_return_url(request.POST)
            return redirect(return_url)
        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, 'register.html', context)


def get_return_url(request_post: dict):
    return_url = request_post.get('return_url')
    return return_url if return_url else 'index'


def login_user(request):
    if request.method == 'GET':
        context = {
            'form': LoginForm,
        }
        return render(request, 'login.html', context)
    else:
        login_form = LoginForm(request.POST)
        return_url = get_return_url(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(return_url)
        context = {
            'form': login_form,
        }
        return render(request, 'login.html', context)


@login_required
def logout_user(req):
    logout(req)
    return redirect('index')


def unauthorized(req):
    return render(req, 'unauthorized.html')
