from django.shortcuts import render
from names.models import Name
from names.serializers import NameSerializer
from rest_framework import generics

class NameListCreate(generics.ListCreateAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer