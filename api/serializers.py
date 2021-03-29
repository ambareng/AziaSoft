from .models import DriversEducation, MedicalProvider, MedicalType

from rest_framework import serializers


class DriversEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriversEducation
        fields = '__all__'


class MedicalProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalProvider
        fields = '__all__'


class MedicalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalType
        fields = '__all__'
