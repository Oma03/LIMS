from rest_framework import generics
# from lim.models import *
from .serializers import *

# Create your views here.


class PatientApi(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class SampleApi(generics.CreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
