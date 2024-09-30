from rest_framework import serializers
from .models import Employee, Attendance

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Employee model.
    """
    class Meta:
        """
        Meta class for EmployeeSerializer.
        """
        model = Employee
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Attendance model.
    """
    class Meta:
        """
        Meta class for AttendanceSerializer.
        """
        model = Attendance
        fields = '__all__'
