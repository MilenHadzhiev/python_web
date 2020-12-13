from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.views.generic import ListView

from untitled.models import Game


def index(request):
    title = 'Django Excercise Project'
    users = User.objects.all()
    groups = Group.objects.all()
    context = {
        'title': title,
        'users': users,
        'groups': groups
    }
    return render(request, 'index.html', context)


class UsersListView(ListView):
    model = User
    template_name = 'index2.html'
    queryset = User.objects.all().order_by('username')

    def get_context_object_name(self, object_list):
        return 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'From class view'
        return context


class GamesListView(ListView):
    model = Game
    template_name = 'games.html'

    def get_context_object_name(self, object_list):
        return 'games'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Games from class view'
        return context
