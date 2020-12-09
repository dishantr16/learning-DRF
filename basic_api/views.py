from django.shortcuts import render
from rest_framework import generics
from basic_api.models import DPost
from basic_api.serializers import DRFPOST
# Create your views here.

class API_Objects(generics.ListCreateAPIView):
    queryset = DPost.objects.all()
    serializer_class = DRFPOST

class API_Objects_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = DPost.objects.all()
    serializer_class = DRFPOST
