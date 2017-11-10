from rest_framework import serializers
from .models import (Patient,
                     Doctor,
                     Enterprise,
                     MedicalHistory,
                     ArtifactMeasurement,
                     )



class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = '__all__'


class DoctorLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'doctor_name', 'picture_url')


class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'
        #depth = 1


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


# without model
class PatientVerifySerializer(serializers.Serializer):
    dni = serializers.CharField(max_length=8)
    enterprise_id = serializers.IntegerField()


# artifact
class ArtifactMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtifactMeasurement
        fields = '__all__'


# class PatientHistorySerializer(serializers.ModelSerializer):
#     medical_histories = serializers.StringRelatedField(many=True)
#     enterprise = serializers.StringRelatedField(many=True)
#
#     class Meta:
#         model = Patient
#         fields = ('contact_phone', 'dni', 'medical_histories')


