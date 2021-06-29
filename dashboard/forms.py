from django import forms
from django.db import models
from food.models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:

        model = Recipe
        print(model)
        fields = "__all__"
        widgets = {
        "title":forms.TextInput(attrs={'class':'form-control'}),
        "description": forms.TextInput(attrs={'class': 'form-control'}),
        "prep_time": forms.TimeInput(attrs={'class': 'form-control'}),
        "cook_time": forms.TimeInput(attrs={'class': 'form-control'}),

        "stars": forms.(attrs={'class': 'form-control'}),

        }
