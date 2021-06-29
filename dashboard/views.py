from django.shortcuts import render, redirect

from food.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from dashboard.forms import *

def dashboard_home_page(request):
    return render(request, 'dashboard/index.html')

def recipe_create(request):
    model = Recipe()
    form = RecipeForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('recipe_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request,'dashboard/recipe/form.html',ctx)




