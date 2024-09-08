# serializers.py

from rest_framework import serializers
from .models import Mail
class EmailSerializer(serializers.Serializer):
    class Meta:
        model = Mail
        fields = '__all__'


