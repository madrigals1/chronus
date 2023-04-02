from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate

from utils.functions import get_token_for_user

from member.serializers import MemberSerializer
from user.models import User, Employee
from member.models import Member
from user.serializers import UserSerializer, EmployeeSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Get all users
        """
        return User.objects.all()

    @action(
        methods=['post'],
        detail=False,
        permission_classes=[AllowAny],
        url_path='get-token'
    )
    def get_token(self, request):
        """
        User can get his token using Email and Password.
        """

        # TODO: Improve logic of receiving tokens, handle token expiration
        body = request.data.get('body')

        email = body.get('email')
        password = body.get('password')

        if email is None or password is None:
            return Response(
                {'error': 'Please provide both username and password'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Authenticate
        user = authenticate(email=email, password=password)

        if not user:
            return Response(
                {'error': 'Invalid Credentials'},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Get token using User ID
        token = get_token_for_user(user.id)

        return Response({'token': token}, status=status.HTTP_201_CREATED)


class UserEmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        """
        Get all employees of a user
        """
        return Employee.objects.filter(user=self.kwargs['user_pk'])


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        """
        Get all employees
        """
        return Employee.objects.select_related('user', 'company')


class EmployeeMemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MemberSerializer

    def get_queryset(self):
        """
        Get all members of an employee
        """
        return (
            Member.objects
            .filter(employee=self.kwargs['employee_pk'])
            .select_related(
                'team',
                'team__company',
                'employee__user',
                'employee__company',
            )
        )

