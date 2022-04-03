from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'date_joined', 'is_active')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('user','title', 'content', 'created_at', 'updated_at')

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'user','title', 'content', 'created_at', 'updated_at')