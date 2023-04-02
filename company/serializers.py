from rest_framework import serializers
from company.models import Company, Team


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'type', 'updated_at', 'created_at']


class TeamSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Team
        fields = ['id', 'name', 'company', 'updated_at', 'created_at']
