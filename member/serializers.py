from rest_framework import serializers
from member.models import Member, Task
from company.serializers import TeamSerializer
from user.serializers import EmployeeSerializer


class MemberSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    team = TeamSerializer()

    class Meta:
        model = Member
        unique_together = ['employee', 'team']
        fields = [
            'id',
            'name',
            'employee',
            'team',
            'updated_at',
            'created_at',
        ]


class TaskSerializer(serializers.ModelSerializer):
    member = MemberSerializer()

    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'type',
            'date',
            'member',
            'updated_at',
            'created_at',
        ]
