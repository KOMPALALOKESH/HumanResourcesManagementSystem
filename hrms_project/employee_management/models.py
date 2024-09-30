from django.db import models

# Create your models here.

class Employee(models.Model):
    """
    Represents an employee in the organization.
    """
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_of_joining = models.DateField()

    def __str__(self):
        """
        Returns the string representation of the Employee instance.
        """
        return self.name

class Attendance(models.Model):
    """
    Represents the attendance record of an employee.
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)
