from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Recipe
        fields = '__all__'

