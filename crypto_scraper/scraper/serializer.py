from rest_framework import serializers
from.models import ScrapingTask

class ScrapingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapingTask
        fields = ["id", "coin", "output", "error", "completed"]