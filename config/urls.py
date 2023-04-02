"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, include
from rest_framework_nested import routers

from company.views import *
from member.views import *
from user.views import *

# /api/v1/
router = routers.DefaultRouter()

# /api/v1/companies/{pk}?
router.register('companies', CompanyViewSet, basename='company')

# /api/v1/companies/{nested}
company_nested_router = routers.NestedSimpleRouter(
    router, 'companies', lookup='company'
)

# /api/v1/companies/{pk}/teams/{pk}?
company_nested_router.register('teams', CompanyTeamViewSet, basename='company-teams')
# /api/v1/companies/{pk}/employees/{pk}?
company_nested_router.register(
    'employees', CompanyEmployeeViewSet, basename='company-employees'
)

# /api/v1/teams/{pk}?
router.register('teams', TeamViewSet, basename='team')

# /api/v1/teams/{nested}
team_nested_router = routers.NestedSimpleRouter(router, 'teams', lookup='team')
# /api/v1/teams/{pk}/members/{pk}?
team_nested_router.register('members', TeamMemberViewSet, basename='team-members')

# /api/v1/members/{pk}?
router.register('members', MemberViewSet, basename='member')

# /api/v1/members/{nested}
member_nested_router = routers.NestedSimpleRouter(router, 'members', lookup='member')
# /api/v1/members/{pk}/tasks/{pk}?
member_nested_router.register('tasks', MemberTaskViewSet, basename='member-tasks')

# /api/v1/tasks/{pk}?
router.register('tasks', TaskViewSet, basename='task')

# /api/v1/users/{pk}?
router.register('users', UserViewSet, basename='user')

# /api/v1/users/{nested}
user_nested_router = routers.NestedSimpleRouter(router, 'users', lookup='user')
# /api/v1/users/{pk}/employees/{pk}?
user_nested_router.register(
    'employees', UserEmployeeViewSet, basename='user-employees'
)

# /api/v1/employees/{pk}?
router.register('employees', EmployeeViewSet, basename='employee')

# /api/v1/employees/{nested}
employee_nested_router = routers.NestedSimpleRouter(
    router, 'employees', lookup='employee'
)
# /api/v1/employees/{pk}/members/{pk}?
employee_nested_router.register(
    'members', EmployeeMemberViewSet, basename='employee-members'
)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(company_nested_router.urls)),
    path('api/v1/', include(team_nested_router.urls)),
    path('api/v1/', include(member_nested_router.urls)),
    path('api/v1/', include(user_nested_router.urls)),
    path('api/v1/', include(employee_nested_router.urls)),
]

# if settings.DEBUG:
#     import debug_toolbar

#     urlpatterns += [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ]
