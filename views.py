from django.shortcuts import render
from names.models import Name, Rating
from names.serializers import NameSerializer, RatingSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

class NameListCreate(generics.ListCreateAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer

    #def handle_integrity_error(self):


    def create(self, request, *args, **kwargs):
        name_serializer = NameSerializer(data=request.data)
        ratings_serializer = RatingSerializer(data=request.data)
        if name_serializer.is_valid():
            try:
                ref_name_id = Name.objects.get(name=name_serializer.validated_data['name'], boy=name_serializer.validated_data['boy']).id
                ratings_serializer.initial_data['fk_name'] = ref_name_id
                if ratings_serializer.is_valid():
                    ratings_serializer.save()
                    return Response(ratings_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(ratings_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Name.DoesNotExist:
                with transaction.atomic():
                    name_serializer.save()
                    ratings_serializer.initial_data['fk_name'] = name_serializer.data['id']
                    if ratings_serializer.is_valid():
                        ratings_serializer.save()
                    else:
                        transaction.set_rollback(True)
                        return Response(ratings_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    name_serializer.data['ratings'].append(ratings_serializer.data)
                    return Response(name_serializer.data, status=status.HTTP_201_CREATED)
        return Response(name_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RatingListCreate(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer