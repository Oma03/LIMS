from django.urls import path
from .views import *

urlpatterns = [
    path('', BookPatient.as_view(), name='home'),
]
