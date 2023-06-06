import datetime

from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
from employees.models import Employee


class EmployeeViewTest(APITestCase):
    def setUp(self):
        self.client = Client()
        self.employee_data = {
            "first_name": "John",
            "last_name": "Doe",
            "mobile_number": "0881234567",
            "start_date": datetime.date.today(),
            "position": Employee.POSITION_JUNIOR_DEVELOPER,
            "salary": "EUR 1",
            "employee_id": "ID 1",
        }

    def test_create_employee(self):
        self.client.post(
            path=reverse("employees:employees-list"), data=self.employee_data
        )
        self.assertTrue(Employee.objects.filter(employee_id="ID 1").exists())

    def test_update_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        self.client.put(
            path=reverse("employees:employees-detail", args=(employee.id,)),
            data={
                "first_name": "New",
                "last_name": "Name",
                "mobile_number": "0881234567",
                "start_date": datetime.date.today(),
                "position": Employee.POSITION_JUNIOR_DEVELOPER,
                "salary": "EUR 1",
                "employee_id": "ID 1",
            },
            content_type="application/json",
        )
        employee.refresh_from_db()
        self.assertEqual(employee.first_name, "New")
        self.assertEqual(employee.last_name, "Name")
