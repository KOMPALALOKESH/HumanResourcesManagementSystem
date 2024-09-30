from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Attendance, Employee
from .serializers import *
from django.db.models import Count

from .serializers import AttendanceSerializer

# Create your views here.

def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})

def report(request):
    report_data = Employee.objects.values('department').annotate(employee_count=Count('id'))
    return render(request, 'report.html', {'report_data': report_data})



@api_view(['POST'])
def add_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Employee added successfully'})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def mark_attendance(request):
    employee_id = request.data.get('employee_id')
    date = request.data.get('date')
    status = request.data.get('status')
    employee = Employee.objects.get(id=employee_id)
    attendance = Attendance.objects.create(employee=employee, date=date, status=status)
    return Response({'message': 'Attendance marked'})

@api_view(['GET'])
def get_attendance(request, employee_id):
    attendance = Attendance.objects.filter(employee__id=employee_id)
    serializer = AttendanceSerializer(attendance, many=True)
    return Response(serializer.data)


