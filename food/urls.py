from django.urls import path
from .views import *
urlpatterns = [
    path("",home_page, name="home"),
    path("contact/",contact_page, name="contact"),
    path("blog/",blog_post_page, name="blog"),
    path("recipe/",recipes_page, name="recipe"),
    path("recipe/<int:recipe_id>/",recipe_post_page, name="recipe_post"),
    path("recipe/",recipes_page, name="recipe"),

]