from django.db import models
from django.utils import timezone

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hire_date = models.DateField() #2024-09-08
    resignation_date = models.DateField(null=True, blank=True) #2024-09-08

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField() #2024-09-08
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.employee} - {self.leave_type}"