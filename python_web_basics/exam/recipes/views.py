from django.shortcuts import render, redirect

from recipes.forms import RecipeForm
from recipes.models import Recipe


def homepage(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'GET':
        recipe_form = RecipeForm()
        context = {
            'recipe_form': recipe_form,
        }
        return render(request, 'create.html', context)
    else:
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            title = recipe_form.cleaned_data['title']
            image_url = recipe_form.cleaned_data['image_url']
            description = recipe_form.cleaned_data['description']
            ingredients = recipe_form.cleaned_data['ingredients']
            time = recipe_form.cleaned_data['time']
            recipe = Recipe(
                title=title,
                image_url=image_url,
                description=description,
                ingredients=ingredients,
                time=time,
            )
            recipe.save()
            return redirect('homepage')
        context = {
            'recipe_form': recipe_form,
        }
        return render(request, 'create.html', context)


def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'recipe': recipe,
        }
        return render(request, 'edit.html', context)
    else:
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe.title = recipe_form.cleaned_data['title']
            recipe.image_url = recipe_form.cleaned_data['image_url']
            recipe.description = recipe_form.cleaned_data['description']
            recipe.ingredients = recipe_form.cleaned_data['ingredients']
            recipe.time = recipe_form.cleaned_data['time']
            recipe.save()
            return redirect('homepage')
        context = {
            'recipe_form': recipe_form,
        }
        return render(request, 'create.html', context)


def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'recipe': recipe,
        }
        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('homepage')


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe.ingredients_list = [ing for ing in recipe.ingredients.split(', ')]
    context = {
        'recipe': recipe,
    }
    return render(request, 'details.html', context)
