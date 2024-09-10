
from rest_framework.generics import GenericAPIView, CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.renderers import TemplateHTMLRenderer

from . import models
from . import serializers


class SetMealDataView(CreateAPIView):
    
    serializer_class=serializers.MealDataSerializer
    queryset=models.MealData.objects.all()