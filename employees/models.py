from django.db import models


class Employee(models.Model):
    POSITION_JUNIOR_DEVELOPER = 1
    POSITION_SENIOR_DEVELOPER = 2
    POSITION_TEAM_LEAD = 3
    POSITION_PROJECT_MANAGER = 4
    POSITION_CEO = 5
    POSITION_CHOICES = (
        (POSITION_JUNIOR_DEVELOPER, "Junior Developer"),
        (POSITION_SENIOR_DEVELOPER, "Senior Developer"),
        (POSITION_TEAM_LEAD, "Team Lead"),
        (POSITION_PROJECT_MANAGER, "Project Manager"),
        (POSITION_CEO, "CEO"),
    )

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    # Set as Charfield in order to support leading zero or country code.
    mobile_number = models.CharField(max_length=20)
    start_date = models.DateField()
    position = models.IntegerField(choices=POSITION_CHOICES)
    salary = models.CharField(max_length=20, help_text="Salary with currency.")
    employee_id = models.CharField(max_length=20, unique=True)
