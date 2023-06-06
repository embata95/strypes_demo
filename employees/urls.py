from django.urls import path
from rest_framework.routers import DefaultRouter

from employees.views import GetEmployees, EmployeeViewSet

app_name = "employees"

router = DefaultRouter()
router.register("", EmployeeViewSet, basename="employees")

urlpatterns = [path("table", GetEmployees.as_view(), name="get_employees_table")]
urlpatterns += router.urls
