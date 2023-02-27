from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=200)
  age = serializers.IntegerField()
  roll = serializers.IntegerField()
  city = serializers.CharField(max_length=200)