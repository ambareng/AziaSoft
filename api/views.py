from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import DriversEducation, MedicalProvider, MedicalType

from .serializers import DriversEducationSerializer, MedicalProviderSerializer, MedicalTypeSerializer


class DriversEducationViewSet(viewsets.ModelViewSet):
    serializer_class = DriversEducationSerializer
    queryset = DriversEducation.objects.all()

    def destroy(self, request, *args, **kwargs):
        drivers_education = self.get_object()
        drivers_education.is_active = False
        drivers_education.save()

        serializer = DriversEducationSerializer(drivers_education)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = DriversEducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicalProviderViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalProviderSerializer
    queryset = MedicalProvider.objects.all()

    def destroy(self, request, *args, **kwargs):
        medical_provider = self.get_object()
        medical_provider.is_active = False
        medical_provider.save()

        serializer = MedicalProviderSerializer(medical_provider)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = MedicalProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicalTypeViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalTypeSerializer
    queryset = MedicalType.objects.all()

    def destroy(self, request, *args, **kwargs):
        medical_type = self.get_object()
        medical_type.is_active = False
        medical_type.save()

        serializer = MedicalTypeSerializer(medical_type)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = MedicalTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
