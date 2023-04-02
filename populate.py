import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

if True:
    from company.models import Company, Team
    from member.models import Member, Task
    from user.models import User, Employee

COMPANY_COUNT = 6
USER_COUNT = 100

# Min, Max values
TEAM_COUNT_RANGE = (1, 6)
EMPLOYEE_COUNT_RANGE = (5, 30)
TASK_COUNT_RANGE = (1, 100)

fake = Faker()

if __name__ == "__main__":
    users = []

    for _ in range(USER_COUNT):
        user = User.objects.create(
            email=fake.email(),
            name=fake.name(),
        )
        print(user)

        users.append(user)

    for _ in range(COMPANY_COUNT):
        company = Company.objects.create(
            name=fake.company(),
            type=random.choice(Company.TYPES)[0],
        )

        employee_count = random.randrange(
            EMPLOYEE_COUNT_RANGE[0],
            EMPLOYEE_COUNT_RANGE[1],
        )

        company_users = []
        employees = []

        for _ in range(employee_count):
            company_user = random.choice(users)

            if company_user in company_users:
                continue

            company_users.append(company_user)

            employee = Employee.objects.create(
                company=company,
                user=company_user,
            )

            employees.append(employee)

        team_count = random.randrange(TEAM_COUNT_RANGE[0], TEAM_COUNT_RANGE[1])

        for _ in range(team_count):
            team = Team.objects.create(
                name=fake.color_name(),
                company=company,
            )

            team_employees = []
            team_employee_count = random.randrange(1, employee_count)

            for _ in range(team_employee_count):
                employee = random.choice(employees)

                if employee in team_employees:
                    continue

                team_employees.append(employee)

                member = Member.objects.create(
                    employee=employee,
                    team=team,
                )

                task_count = random.randrange(TASK_COUNT_RANGE[0], TASK_COUNT_RANGE[1])

                for _ in range(task_count):
                    task = Task.objects.create(
                        type=random.choice(Task.TYPES)[0],
                        name=fake.sentence(),
                        date=fake.date_this_month(),
                        member=member,
                    )





