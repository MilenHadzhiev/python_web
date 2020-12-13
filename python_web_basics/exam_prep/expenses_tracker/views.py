from django.shortcuts import render, redirect

from expenses_tracker.forms import ExpenseForm, ProfileForm
from expenses_tracker.models import Profile, Expense


def calculate_budget(profile, expenses):
    return profile.budget - sum(expense.price for expense in expenses)


def homepage(request):
    profile = Profile.objects.all()[0]
    if profile:
        expenses = Expense.objects.all()
        profile.budget_left = calculate_budget(profile, expenses)
        context = {
            'profile': profile,
            'expenses': expenses,
        }
        return render(request, 'home-with-profile.html', context)
    profile_form = ProfileForm()
    context = {
        'profile_form': profile_form,
    }
    return render(request, 'home-no-profile.html', context)


def expense_create(request):
    profile = Profile.objects.all()[0]
    if request.method == 'GET':
        expense_form = ExpenseForm()
        context = {
            'expense_form': expense_form,
        }
        return render(request, 'expense-create.html', context)
    else:
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            title = expense_form.cleaned_data['title']
            image_url = expense_form.cleaned_data['image_url']
            description = expense_form.cleaned_data['description']
            price = expense_form.cleaned_data['price']
            expense = Expense(
                title=title,
                image_url=image_url,
                description=description,
                price=price
            )
            expense.save()
            return redirect(homepage)
        context = {
            'expense_form': expense_form,
        }
        return render(request, 'expense-create.html', context)


def expense_edit(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        expense_form = ExpenseForm()
        context = {
            'expense': expense,
            'expense_form': expense_form,
        }
        return render(request, 'expense-edit.html', context)
    else:
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense.title = expense_form.cleaned_data['title']
            expense.description = expense_form.cleaned_data['description']
            expense.image_url = expense_form.cleaned_data['image_url']
            expense.price = expense_form.cleaned_data['price']
            expense.save()
            return redirect('home page')
        context = {
            'expense': expense,
            'expense_form': expense_form,
        }
        return render(request, 'expense-edit.html', context)


def expense_delete(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'expense': expense,
        }
        return render(request, 'expense-delete.html', context)
    else:
        expense.delete()
        return redirect(homepage)


def profile(request):
    if request.method == 'GET':
        profile = Profile.objects.all()[0]
        expenses = Expense.objects.all()
        profile.budget_left = calculate_budget(profile, expenses)
        context = {
            'profile': profile,
        }
        return render(request, 'profile.html', context)
    else:
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            budget = profile_form.cleaned_data['budget']
            first_name = profile_form.cleaned_data['first_name']
            last_name = profile_form.cleaned_data['last_name']
            profile = Profile(budget=budget, first_name=first_name, last_name=last_name)
            profile.save()
            return redirect('home page')


def profile_edit(request):
    profile = Profile.objects.all()[0]
    if request.method == 'GET':
        profile_form = ProfileForm()
        context = {
            'profile': profile,
            'profile_form': profile_form,
        }
        return render(request, 'profile-edit.html', context)
    else:
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile.budget = profile_form.cleaned_data['budget']
            profile.first_name = profile_form.cleaned_data['first_name']
            profile.last_name = profile_form.cleaned_data['last_name']
            profile.save()
            return redirect('profile page')
        context = {
            'profile': profile,
            'profile_form': profile_form,
        }
        return render(request, 'profile-edit.html', context)


def profile_delete(request):
    if request.method == 'GET':
        return render(request, 'profile-delete.html')
    else:
        profile = Profile.objects.all()[0]
        [expense.delete() for expense in Expense.objects.all()]
        profile.delete()
        return render(request, 'home-no-profile.html')
