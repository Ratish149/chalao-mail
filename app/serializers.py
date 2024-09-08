# serializers.py

from rest_framework import serializers
from .models import Mail
class EmailSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()


