from django.urls import path
from .views import *

urlpatterns = [
    path('', PatientApi.as_view()),
]
