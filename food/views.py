# MY comment
from django.shortcuts import render
from .models import *
from  .forms import *
def home_page(request):
    stars=[1,2,3,4,5]
    recipes = Recipe.objects.all()
    for r in recipes:
        print("url= ",r.image)
    form1=CustomerMail(request.POST or None)
    if request.POST and form1.is_valid():
        form1.save()
    ctx={
        "stars":stars,
        "recipes":recipes,
        "form1":form1

    }
    return render(request,"food/index.html",ctx)

def contact_page(request):
    form = CustomerForm(request.POST or None)
    form1=CustomerMail(request.POST or None)
    if request.POST and form.is_valid() and form1.is_valid():
        form.save()
        form1.save()
    ctx={
        "form":form,
        "form1":form1

    }
    return render(request,"food/contact.html",ctx)

def blog_post_page(request):
    blog=Blog.objects.all()
    form1=CustomerMail(request.POST or None)
    if request.POST and form1.is_valid():
        form1.save()
    ctx={
        "blog":blog,
        "form1":form1

    }
    return render(request,"food/blog-post.html", ctx)

def recipe_post_page(request, recipe_id):
    form = CustomerForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
    stars=[1,2,3,4,5]
    recipe = Recipe.objects.get(pk=recipe_id)
    myrecipes = Recipe.objects.all()
    steps = Step.objects.filter(recipe_id=recipe_id)
    ingredients = Ingredient.objects.filter(recipe_id=recipe_id)

    ctx = {
        "stars": stars,
        "recipe": recipe,
        "myrecipes": myrecipes,
        "steps": steps,
        "ingredients": ingredients,
        "form":form
    }
    return render(request,"food/receipe-post.html", ctx)

def recipes_page(request):
    recipes = Recipe.objects.all()
    stars=[1,2,3,4,5]

    ctx = {
        "recipes":recipes,
        "stars": stars
    }
    return render(request,"food/receipes.html",ctx)

# Create your views here.
