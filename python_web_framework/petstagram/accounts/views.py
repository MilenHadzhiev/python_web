from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm, UserProfileImageForm
from accounts.models import UserProfile
from pets.models import Pet


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    pets = Pet.objects.filter(user=user.userprofile).all()
    if request.method == 'GET':
        context = {
            'profile_user': user,
            'pets': pets,
            'form': UserProfileImageForm,
            'can_upload_pic': pk is None,
        }
        return render(request, 'accounts/user_profile.html', context)
    else:
        form = UserProfileImageForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current user profile')
        return redirect('current user profile')


def signup_user(request):
    if request.method == 'GET':
        context = {
            'form': SignUpForm,
        }
        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user=user,
            )
            profile.save()
            login(request, user)
            return redirect('current user profile')
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)


def signout_user(request):
    logout(request)
    return redirect('landing_page')
