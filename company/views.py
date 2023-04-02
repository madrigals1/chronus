from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from company.models import Company, Team
from user.models import Employee
from member.models import Member

from company.serializers import CompanySerializer, TeamSerializer
from user.serializers import EmployeeSerializer
from member.serializers import MemberSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer

    def get_queryset(self):
        """
        Get all companies
        """
        return Company.objects.all()


class CompanyTeamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamSerializer

    def get_queryset(self):
        """
        Get all team of a company
        """
        return Team.objects.filter(company=self.kwargs['company_pk']).select_related(
            'company'
        )


class CompanyEmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        """
        Get all employees of a company
        """
        return (
            Employee.objects
            .filter(company=self.kwargs['company_pk'])
            .select_related('company', 'user')
        )


class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamSerializer

    def get_queryset(self):
        """
        Get all teams
        """
        return Team.objects.select_related('company')


class TeamMemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MemberSerializer

    def get_queryset(self):
        """
        Get all employees of a user
        """
        return Member.objects.filter(team=self.kwargs['team_pk']).select_related(
            'employee__user',
            'employee__company',
            'team__company',
        )
