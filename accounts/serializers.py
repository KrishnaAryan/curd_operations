from rest_framework import serializers
from .models import *
from django.db.models import fields

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields= '__all__'
     