from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from member.models import Member, Task
from member.serializers import MemberSerializer, TaskSerializer


class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MemberSerializer
    serializer_classes = {
        "default": MemberSerializer,
        "read_only": MemberReadOnlySerializer,
    }

    def get_queryset(self):
        """
        Get all users
        """
        return Member.objects.select_related(
            'team',
            'team__company',
            'employee__user',
            'employee__company',
        )


class MemberTaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Get all users
        """
        return Task.objects.filter(member=self.kwargs['member_pk']).select_related(
            'member__employee',
            'member__team',
            'member__employee__company',
            'member__employee__user',
            'member__team__company',
        )


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Get all users
        """
        return Task.objects.select_related(
            "member__employee",
            "member__team",
            "member__employee__company",
            "member__employee__user",
            "member__team__company",
        )
