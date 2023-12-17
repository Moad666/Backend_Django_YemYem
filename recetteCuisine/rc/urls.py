from django.urls import path,include
from .views import *

urlpatterns = [
    path('logout/',logOut, name="logout"),
    path('user_profile/',user_profile, name="user_profile"),
    path('is_superuser/', IsSuperuserView.as_view(), name='is_superuser'),

]