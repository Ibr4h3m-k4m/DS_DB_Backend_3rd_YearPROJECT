from django.core.mail import send_mass_mail, mail_admins, BadHeaderError, EmailMessage
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from djoser.views import UserViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.viewsets import ModelViewSet , GenericViewSet
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from djoser.views import UserViewSet as BaseUserViewSet
from django.conf import settings

from . import serializers, models, permissions


"""
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ViewModifyProjectSerializer
    permission_classes = [permissions.IsProjectLeaderOrAuthenticatedUser]
    
    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return CreateProjectSerializer
        return ViewModifyProjectSerializer

"""
        
class EtablissementViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']
    queryset = models.Etablissement.objects.all()
    serializer_class = serializers.EtablissementSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
    
    def get_permissions(self):
        if self.request.method in ['POST','PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [AllowAny()]
    
    
class StudentViewSet(ModelViewSet):
    queryset = models.Student.objects.select_related('établissement').all()
    serializer_class = serializers.StudentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['établissement_id']
    search_fields = ['user__email']
    
    @action(detail=False, methods=['GET', 'PUT', 'PATCH'], permission_classes=[IsAuthenticated])
    def me(self, request):
        student = models.Student.objects.get(
            user_id=request.user.id
        )
        if request.method == 'GET':
            serializer = serializers.StudentSerializer(student)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = serializers.StudentSerializer(student, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'PATCH':
            serializer = serializers.BaseStudentSerializer(student, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        



class TeacherViewSet(ModelViewSet):
    queryset = models.Teacher.objects.select_related('établissement').all()
    serializer_class = serializers.TeacherSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['établissement_id']
    search_fields = ['user__email']
    
    
    @action(detail=False, methods=['GET', 'PUT', 'PATCH'], permission_classes=[IsAuthenticated])
    def me(self, request):
        teacher = models.Teacher.objects.get(
            user_id=request.user.id
        )
        if request.method == 'GET':
            serializer = serializers.TeacherSerializer(teacher)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = serializers.TeacherSerializer(teacher, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'PATCH':
            serializer = serializers.BaseTeacherSerializer(teacher, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    
    
######## Project Deposition


class PeriodViewSet(ModelViewSet):
    queryset = models.Period.objects.all()  
    serializer_class = serializers.PeriodSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['date_début', 'date_fin']
    

    
    
class ProjectInvitationViewSet(ModelViewSet):
    queryset = models.ProjectInvitation.objects.all()
    serializer_class = serializers.ProjectInvitationSerializer
    filter_backends = [SearchFilter]
    search_fields = ['email']
    
    
class ProjectTeamViewSet(ModelViewSet):
    queryset = models.ProjectTeam.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['participants']
    search_fields = ['name', 'participants__user__email']
    
    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return serializers.CreateProjectTeamSerializer
        elif self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return serializers.ProjectTeamSerializer
        
    
    
class ManagementTeamViewSet(ModelViewSet):
    queryset = models.ManagementTeam.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['superviseur', 'co_superviseur']
    search_fields = ['superviseur__user__email', 'co_superviseur__user__email']
    
    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return serializers.CreateManagementTeamSerializer
        elif self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return serializers.ManagementTeamSerializer
    
class ProjectTypeViewSet(ModelViewSet):
    queryset = models.ProjectType.objects.all()
    serializer_class = serializers.ProjectTypeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['type', 'intitulé_idée_innovante']
    
    
class ProjectViewSet(ModelViewSet):
    queryset = models.Project.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['établissement_id', 'period_id', 'porteur_student_id',
                        'porteur_teacher_id', 'project_team_id', 'équipe_encadrement_id']
    search_fields = ['title', 'status', 'résumé', 'porteur_student__user__email',
                     'porteur_teacher__user__email', 'project_team__team_leader__user__username',
                     'project_team__team_leader__user__email',
                     'équipe_encadrement__superviseur__user__email',
                     'équipe_encadrement__co_superviseur__user__email',]
    ordering_fields = ['deposition_date']
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH', 'POST']:
            return serializers.CreateProjectSerializer
        elif self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return serializers.ProjectSerializer
    
    
######## Project Validation


class ValidationCommitteeViewSet(ModelViewSet):
    queryset = models.ValidationCommittee.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['établissement_id', 'members']
    search_fields = ['établissement__name']
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateValidationCommitteeSerializer
        elif self.request.method in ['PUT', 'PATCH', 'GET', 'HEAD', 'OPTIONS']:
            return serializers.ValidationCommitteeSerializer
    
class DecisionOfCommitteeViewSet(ModelViewSet):
    
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = models.DecisionOfCommittee.objects.all()
    serializer_class = serializers.DecisionOfCommitteeSerializer
    
    
class ProjectValidationViewSet(ModelViewSet):
    queryset = models.ProjectValidation.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['project_id', 'committee_id', 'decision_id']
    search_fields = ['project__établissement__name', 'project__status']
    ordering_fields = ['validation_date']
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateProjectValidationSerializer
        elif self.request.method in ['PUT', 'PATCH', 'GET', 'HEAD', 'OPTIONS']:
            return serializers.ProjectValidationSerializer
    

#### gestion recours

class RecoursViewSet(ModelViewSet):

    queryset = models.Recours.objects.all()
    serializer_class = serializers.RecoursSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['period_id']
    search_fields = ['title']
    ordering_fields = ['date_deposition']


class RecoursValidationViewSet(ModelViewSet):
    queryset = models.RecoursValidation.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['recours_id', 'validated_project_id']
    search_fields = ['validated_project__project__title']
    ordering_fields = ['recours__date_deposition']
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateRecoursValidationSerializer
        elif self.request.method in ['PUT', 'PATCH', 'GET', 'HEAD', 'OPTIONS']:
            return serializers.RecoursValidationSerializer   
        
            






    
    
    
    