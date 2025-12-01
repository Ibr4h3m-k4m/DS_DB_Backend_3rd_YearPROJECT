from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .models import Project, Student, Teacher
"""
class IsProjectAdminOrMemberReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try: 
            porteur_student = Student.objects.get(user=request.user)
            porteur=porteur_student
        except Student.DoesNotExist:
            try: 
                porteur_teacher = Teacher.objects.get(user=request.user)
                porteur
            except Teacher.DoesNotExist:
                return False
        proj= Project.objects.get()
        if request.method in permissions.SAFE_METHODS:
            return True
        

class IsProjectMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            pmem = ProjectMembership.objects.get(member=request.user, project=obj)
        except ProjectMembership.DoesNotExist:
            return False
        return True
        
        """
"""     
class IsCommittee(permissions.BasePermission) :
    def has_object_permission(self, request, view, obj):
        try:
            teacher=Teacher.objects.get(user=request.user)    
        except Teacher.DoesNotExist:
            return False
        return teacher.is_membre_of_commité   """   