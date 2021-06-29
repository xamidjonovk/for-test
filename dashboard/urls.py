from django.urls import path
from .views import *
urlpatterns = [
    path('', dashboard_home_page, name='dashboard_home_page'),
    path('recipe/', recipe_create, name='recipe_create'),
    # path('dashboard/login_page/', login_page, name='login_page'),
    # path('dashboard/logout_page/', logout_page, name='logout_page'),
    #
    # path('dashboard/recipe/create/', recipe_create, name='recipe_create'),
    # path('dashboard/recipe/<int:pk>/edit/', recipe_edit, name='recipe_edit'),
    # path('dashboard/recipe/<int:pk>/delete/', recipe_delete, name='recipe_delete'),
    # path('dashboard/recipe/list/', recipe_list, name='recipe_list'),
]