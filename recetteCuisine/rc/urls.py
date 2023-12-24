from django.urls import path,include
from .views import *

urlpatterns = [
    path('logout/',logOut, name="logout"),
    path('user_profile/',user_profile, name="user_profile"),
    path('is_superuser/', IsSuperuserView.as_view(), name='is_superuser'),

    # Recipes
    path('create_recipe/', RecipeListCreateView.as_view(), name='create_recipe'),
    path('list_recipe/', RecipeAllListView.as_view(), name='list_recipe'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),

    # Users
    path('create_user/', UserListCreateView.as_view(), name='create_user'),
    path('list_user/', UserAllListView.as_view(), name='list_user'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

]