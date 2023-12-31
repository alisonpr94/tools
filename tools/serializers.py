from rest_framework import serializers
from .models import Tool

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ['id', 'title', 'link', 'description', 'tags']