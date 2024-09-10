from django.urls import path
from . import views
urlpatterns=[
    path('setup/',views.SetMealDataView.as_view(),),

]