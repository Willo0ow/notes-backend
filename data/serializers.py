from rest_framework import serializers
from . models import *




class NotesSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """

    class Meta:
        model = Note
        fields = ('id', 'user','title', 'content', 'created_at', 'updated_at')