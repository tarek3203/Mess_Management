from django import forms
from . import models

class MealDataForm(forms.ModelForm):
    class Meta:
        model = models.MealData
        fields = ["date", 'launch', 'dinner']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})