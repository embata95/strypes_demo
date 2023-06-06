from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    # Set as Charfield in order to support leading zero or country code.
    mobile_number = models.CharField(max_length=20)
    start_date = models.DateField()
    salary = models.CharField(max_length=20)
    employee_id = models.CharField(max_length=20, unique=True)
