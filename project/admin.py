from django.contrib import admin
from core import models as coremodels
from . import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'num_inscription','établissement']
    list_per_page = 10
    list_filter = ['établissement']
    list_select_related = ['user']
    
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name', 'last_name', 'num_inscription']


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'matricule', 'is_president_of_commité', 'is_membre_of_commité']
    list_per_page = 10
    list_select_related = ['user']
    list_filter = ['is_president_of_commité', 'is_membre_of_commité', 'établissement']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name', 'last_name', 'matricule']

    
class StudentInline(admin.StackedInline):
    model = models.Student


############ Soumission des projets ##########

@admin.register(models.Etablissement)
class EtablissementAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo_preview']
    inlines = [StudentInline]
    search_fields = ['name']


@admin.register(models.Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_début', 'date_fin']
    search_fields = ['name']
    list_filter = ['name']
    
    
@admin.register(models.ProjectInvitation)    
class ProjectInvitationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'consumed'] 
    search_fields = ['email']
    
@admin.register(models.ProjectTeam)    
class ProjectTeamAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']       
    
@admin.register(models.ManagementTeam)    
class ManagementTeamAdmin(admin.ModelAdmin):   
    list_display = ['name', 'superviseur']
    search_fields = ['name']
    
@admin.register(models.ProjectType)    
class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'intitulé_idée_innovante']
    search_fields = ['intitulé_idée_innovante']
    list_filter = ['type']
    
    
         

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        
        (("Project info"), {"fields": ("title","établissement", "project_type", "status",
                                         "résumé",
                                        )}),
        (
            ("Project personnel"),
            {
                "fields": (
                    "porteur_student",
                    "porteur_teacher",
                    "project_team",
                    "équipe_encadrement",
                ),
            },
        ),
    
        (("Important dates"), {"fields": ("period",)}),
    )
    autocomplete_fields = ['établissement', 'project_type', 'porteur_student',
                           'porteur_teacher', 'project_team', 'équipe_encadrement']
    list_display = ['title','status','period',
                    'établissement', 'project_team', 'équipe_encadrement']
    list_filter = ['status', 'établissement']
    list_per_page = 10
    search_fields = ['title','project_team']
    

################## validation des projets ############
@admin.register(models.ValidationCommittee)
class ValidationCommitteeAdmin(admin.ModelAdmin):
    list_filter = ['établissement']
    search_fields = ['description']
    
    
 
@admin.register(models.DecisionOfCommittee)    
class DecisionOfCommitteeAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']  
    search_fields = ['title']
    
@admin.register(models.ProjectValidation)    
class ProjectValidationAdmin(admin.ModelAdmin):
    list_display = ['project', 'committee', 'decision', 'validation_date']
    list_filter = ['decision', 'committee']
    search_fields = ['project']      
    list_per_page = 10  


@admin.register(models.Recours)
class RecoursAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_deposition', 'period']
    list_filter = ['period']
    

@admin.register(models.RecoursValidation)    
class RecoursValidationAdmin(admin.ModelAdmin):
    list_filter = ['recours']
    
