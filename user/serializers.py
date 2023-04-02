from rest_framework import serializers
from user.models import User, Employee
from company.serializers import CompanySerializer


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )

    password = serializers.CharField(
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password', 'updated_at']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_email(self, value):
        check_query = User.objects.filter(email=value)
        if self.instance:
            check_query = check_query.exclude(pk=self.instance.pk)

        if self.parent is not None and self.parent.instance is not None:
            user = getattr(self.parent.instance, self.field_name)
            check_query = check_query.exclude(pk=user.pk)

        if check_query.exists():
            raise serializers.ValidationError('User with given email already exists')
        return value


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    company = CompanySerializer()

    class Meta:
        model = Employee
        unique_together = ['user', 'company']
        fields = [
            'id',
            'user',
            'company',
            'updated_at',
            'created_at',
        ]
