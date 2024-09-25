# serializers.py
from rest_framework import serializers
from .models import VisitorTable

class VisitorTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorTable
        fields = '__all__'

