from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from pets.forms import PetCreateForm, CommentForm
from pets.models import Pet, Like, Comment


def landing_page(request):
    if request.user.id:
        return redirect('current user profile')
    return render(request, 'landing_page.html')


def pets_all(request):
    pets = Pet.objects.all().order_by('name')
    context = {
        'pets': pets,
    }
    return render(request, 'pet_list.html', context)


@login_required
def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        like = Like(pk)
        comment_form = CommentForm()
        context = {
            'pet': pet,
            'like': like,
            'comment_form': comment_form,
            'can_change': request.user == pet.user.user,
            'can_like': request.user != pet.user.user,
            'has_liked': pet.like_set.filter(user_id=request.user.userprofile.id).exists(),
            'can_comment': request.user != pet.user.user,
        }
        return render(request, 'pet_detail.html', context)
    else:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(comment=comment_form.cleaned_data['comment'])
            comment.pet = pet
            comment.user = request.user.userprofile
            comment.save()
            return redirect('pet details', pk)
        context = {
            'pet': pet,
            'comment_form': comment_form,
        }
        return render(request, 'pet_detail.html', context)


@login_required
def pet_like(request, pk):
    like = Like.objects.filter(user_id=request.user.userprofile.id, pet_id=pk).first()
    if like:
        like.delete()
    else:
        pet = Pet.objects.get(pk=pk)
        like = Like(test=str(pk), user=request.user.userprofile)
        like.pet = pet
        like.save()
    return pet_details(request, pk)


@login_required
def create_pet(request, pet_form=None, form_action='create pet', pk=None):
    if request.method == 'GET':
        if not pet_form:
            pet_form = PetCreateForm()
        context = {
            'pet_form': pet_form,
            'form_action': form_action,
            'pk': pk,
        }
        return render(request, 'pet_create.html', context)
    else:
        pet_form = PetCreateForm(request.POST, request.FILES)
        if pet_form.is_valid():
            pet = pet_form.save(commit=False)
            pet.user = request.user.userprofile
            pet.save()
            return redirect('all pets')
        context = {
            'pet_form': pet_form
        }
        return render(request, 'pet_create.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        pet_form = PetCreateForm(initial=pet.__dict__)
        context = {
            'pet': pet,
            'pet_form': pet_form,
        }
        return render(request, 'pet_edit.html', context)
    else:
        pet_form = PetCreateForm(request.POST, request.FILES)
        if pet_form.is_valid():
            pet = pet_form.save()
            pet.save()
            return redirect('all pets')
        return create_pet(
            request,
            pet_form=pet_form,
            form_action='edit pet',
            pk=pk
        )


@login_required
def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
        }
        return render(request, 'pet_delete.html', context)
    pet.delete()
    return redirect('all pets')
