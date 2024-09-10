from rest_framework import serializers
from django.utils import timezone
from datetime import timedelta
from . import models

def tomorrow():
    return timezone.now().date() + timedelta(days=1)

class MealDataSerializer(serializers.ModelSerializer):
    date = serializers.DateField(default=tomorrow, )

    class Meta:
        model = models.MealData
        fields = ["date", 'launch', 'dinner']
