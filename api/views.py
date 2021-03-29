from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from .models import DriversEducation, MedicalProvider, MedicalType

from .serializers import DriversEducationSerializer, MedicalProviderSerializer, MedicalTypeSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1  # 1 only for now just to see it
    page_size_query_param = 'page_size'
    max_page_size = 100


class DriversEducationViewSet(viewsets.ModelViewSet):
    serializer_class = DriversEducationSerializer
    queryset = DriversEducation.objects.all()
    search_fields = ['instructor', 'school']
    filter_backends = (filters.SearchFilter,)
    pagination_class = StandardResultsSetPagination

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

    def get_queryset(self):
        queryset = DriversEducation.objects.all()
        school = self.request.query_params.get('school')
        instructor = self.request.query_params.get('instructor')
        if school is not None:
            queryset = queryset.filter(school=school)
        if instructor is not None:
            queryset = queryset.filter(instructor=instructor)
        return queryset


class MedicalProviderViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalProviderSerializer
    queryset = MedicalProvider.objects.all()
    search_fields = ['name', 'address', 'contact_person', 'contact_person_address']
    filter_backends = (filters.SearchFilter,)
    pagination_class = StandardResultsSetPagination

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

    def get_queryset(self):
        queryset = MedicalProvider.objects.all()
        medical_type = self.request.query_params.get('medical_type')
        if medical_type is not None:
            queryset = queryset.filter(medical_type=medical_type)
        return queryset


class MedicalTypeViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalTypeSerializer
    queryset = MedicalType.objects.all()
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    pagination_class = StandardResultsSetPagination

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

    def get_queryset(self):
        queryset = MedicalType.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset
