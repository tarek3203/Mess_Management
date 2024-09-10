from typing import Iterable
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User=get_user_model()
# Create your models here.
class MealData(models.Model) :
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()
    launch=models.PositiveSmallIntegerField(default=0)
    dinner=models.PositiveSmallIntegerField(default=0)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    @property
    def count(self):
        return self.launch+self.dinner
    
    def save(self, *args,**kwargs):
        now=timezone.now()
        if now<self.date:
            return super().save(*args,**kwargs)