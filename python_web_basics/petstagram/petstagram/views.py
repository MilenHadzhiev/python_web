from django.shortcuts import render, redirect

from pets.models import Pet, Like


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def pet_list(request):
    pets = Pet.objects.all()
    context = {
        'pets': pets,
    }
    return render(request, 'pet_list.html', context)


def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    context = {
        'pet': pet
    }
    return render(request, 'pet_detail.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(test=str(pk))
    like.pet = pet
    like.save()
    return redirect(f'../details/{pet.id}')
