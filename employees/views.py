from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class GetEmployees(ListView):
    model = Employee
    template_name = "list_employees.html"


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
