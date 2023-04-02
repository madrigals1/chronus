from django.db import models


class Member(models.Model):
    employee = models.ForeignKey(
        'user.Employee', on_delete=models.CASCADE, related_name='members'
    )
    team = models.ForeignKey(
        'company.Team', on_delete=models.CASCADE, related_name='members'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def team_name(self):
        return self.team.name

    @property
    def employee_name(self):
        return self.employee.user.name

    @property
    def name(self):
        return f'{self.team_name} -  {self.employee_name}'

    def __str__(self):
        return self.name


class Task(models.Model):
    TYPES = [
        ('yesterday', 'Yesterday'),
        ('today', 'Today'),
        ('block', 'Block Reasons')
    ]

    name = models.CharField(max_length=100, blank=False, default='')
    date = models.DateField()
    type = models.CharField(max_length=32, choices=TYPES, default='today')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    member = models.ForeignKey(
        'member.Member', on_delete=models.CASCADE, related_name='tasks'
    )

    @property
    def member_name(self):
        return self.member.name

    def __str__(self):
        return self.name

