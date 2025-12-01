from django.contrib import admin
from django.conf import settings
from django.db import models
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _


class Etablissement(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    logo = models.ImageField(upload_to='project/images', null=True, blank=True)

    def logo_preview(self): #new
            return mark_safe(f'<img src = "{self.logo.url}" width="100px" height= "100px" object-fit="cover"/>')
    
    def __str__(self) -> str:
         return self.name


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    établissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE, blank=True, null=True)
    num_inscription = models.BigIntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='project/images', null=True, blank=True)
    filiére = models.CharField(max_length=255, null=True, blank=True)
    spécialité = models.CharField(max_length=100, null=True, blank=True)
    
    def profile_picture_preview(self): #new
            return mark_safe(f'<img src = "{self.profile_picture.url}" width="100px" height= "100px" object-fit="cover"/>')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
     
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    def user__email(self):
        return self.user.email
    class Meta:
        ordering = ['user__first_name', 'user__last_name'] 


class Teacher(models.Model):

    PROFESSEUR = 'Professeur'
    MAITRE_DE_CONFERENCES_A = 'Maître de conférences A'
    MAITRE_DE_CONFERENCES_B = 'Maître de conférences B'
    MAITRE_ASSISTANT_A = 'Maître assistant A'
    MAITRE_ASSISTANT_B = 'Maître assistant B'
    
    GRADE_CHOICES = [
    (PROFESSEUR,'Professeur'),
    (MAITRE_DE_CONFERENCES_A,'Maître de conférences A'),
    (MAITRE_DE_CONFERENCES_B,'Maître de conférences B'),
    (MAITRE_ASSISTANT_A , 'Maître assistant A'),
    (MAITRE_ASSISTANT_B , 'Maître assistant B'),
]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    établissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE, blank=True, null=True)
    is_president_of_commité = models.BooleanField(_('Présidant de l\'incubateur ?'), default=False, help_text=_('Si cet enseignant est un présidant dans une comité'), ) #new
    is_membre_of_commité = models.BooleanField(_('Membre de la commité ?'), default=False, help_text=_('Si cet enseignant est un membre dans une comité'), )#new
    matricule = models.BigIntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='project/images', null=True, blank=True)
    grade = models.CharField(max_length=255, choices=GRADE_CHOICES)
    spécialité = models.CharField(max_length=100, null=True, blank=True)
    
    def profile_picture_preview(self): #new
            return mark_safe(f'<img src = "{self.profile_picture.url}" width="100px" height= "100px" object-fit="cover"/>')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
     
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    def user__email(self):
        return self.user.email
    class Meta:
        ordering = ['user__first_name', 'user__last_name'] 

##################  Sprint 2  : Project deposition ########################################################################

class Period(models.Model):
    
    SOUMISSION_PROJET = 'période de soumission des projets'
    VALIDATION_PROJET = 'période de validation des projet'
    DEPOT_RECOURS = 'période de dépôt des recours'
    VALIDATION_PROJET_APRES_RECOURS = 'période da validation des projets aprés recours'
    
    PERIOD_CHOICES = [
        (SOUMISSION_PROJET, 'période de soumission des projets'),
        (VALIDATION_PROJET, 'période de validation des projet'),
        (DEPOT_RECOURS, 'période de dépôt des recours'),
        (VALIDATION_PROJET_APRES_RECOURS, 'période da validation des projets aprés recours')
    ]

    
    name = models.CharField(max_length=255, choices= PERIOD_CHOICES)
    description = models.TextField(blank=True)
    date_début = models.DateField()
    date_fin = models.DateField()
    
    
    def __str__(self) -> str:
         return self.name

     
    
    
class ProjectInvitation(models.Model):  #pour invité les membres
    SUPERVISEUR = 'invitation de participation pour la supervision'
    STUDENT = 'invitation de participation dans une équipe de projet'
    
    INVITATION_CHOICES = [
        (SUPERVISEUR, 'invitation de participation pour la supervision'),
        (STUDENT, 'invitation de participation dans une équipe de projet' )
    ]
    
    name = models.CharField(max_length=255, choices=INVITATION_CHOICES)
    description = models.TextField(blank=True)
    email = models.EmailField()  
    consumed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.name}: {self.email}'    
           
class ProjectTeam(models.Model):
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(Student, blank=True )
    
    
    def __str__(self) -> str:
        return self.name
    
class ManagementTeam(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    superviseur = models.ForeignKey(Teacher, on_delete=models.PROTECT,  blank=True, null=True, related_name='superviseur')
    co_superviseur = models.ForeignKey(Teacher, on_delete=models.PROTECT, blank=True, null=True, related_name='co_superviseur')
    
    def __str__(self) -> str:
         return self.name

class ProjectType(models.Model):
    
    STARTUP = 'un diplôme - une startup'
    PATENT = 'Un diplôme - Un Brevet'

    PROJECT_TYPE_CHOICES = [
        (STARTUP,'un diplôme - une startup'),
        (PATENT,'Un diplôme - Un Brevet')
    ]
         
    type = models.CharField(max_length=50, choices=PROJECT_TYPE_CHOICES, help_text=_('Select the type of the project'),)
    intitulé_idée_innovante = models.CharField(max_length=255)
    
    def __str__(self) -> str:
         return f'{self.type}: {self.intitulé_idée_innovante}'

class Project (models.Model):
    
    ACTIVE = 'Active'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'
    ON_HOLD = 'On Hold'
    REJECTED = 'Rejected'
    
    PROJECT_STATUS_CHOICES = [
    (ACTIVE,'Active'),
    (COMPLETED,'Completed'),
    (CANCELLED,'Cancelled'),
    (ON_HOLD,'On Hold'),
    (REJECTED,'Rejected'),
]


    
    title = models.CharField(max_length=255)
    project_type = models.OneToOneField(ProjectType, on_delete=models.PROTECT)
    établissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=PROJECT_STATUS_CHOICES, default=ON_HOLD)
    period = models.ForeignKey(Period, on_delete=models.PROTECT)
    deposition_date = models.DateField(auto_now_add=True)
    porteur_student = models.OneToOneField(Student, on_delete=models.CASCADE, blank=True, null=True)
    porteur_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    project_team = models.OneToOneField(ProjectTeam, on_delete=models.PROTECT , related_name='équipe_projet',  blank=True, null=True)
    équipe_encadrement = models.ForeignKey(ManagementTeam, on_delete=models.PROTECT, related_name='équipe_encadrement', blank=True, null=True)

    résumé = models.TextField(blank=True)
   
    
    def __str__(self) -> str:
        return f'{self.title}-{self.project_type.type}: {self.project_type.intitulé_idée_innovante}'
   
###################### Project validation ##########################
class ValidationCommittee(models.Model):
 
    description = models.TextField(blank=True)
    members = models.ManyToManyField(Teacher) # the president is included in the membres but should have the field "is_president_of_comitte"
                                              # in his teacher profile set to true so we dont need a new profile, neither do we need to inctanciate the teachers class twice in the same table
                                              
    établissement = models.OneToOneField(Etablissement, on_delete=models.CASCADE) 
    

    
    def __str__(self) -> str:
         return f'{self.établissement.name} scientifique committe'
    
 
 
class DecisionOfCommittee(models.Model):
    
    
    AVIS_FAVORABLE = 'Avis favorable'
    AVIS_DEFAVORABLE = 'Avis défavorable'
    ACCEPTE_SOUS_RESERVES_MINEURS = 'Accepté sous réserves mineurs'
    ACCEPTE_SOUS_RESERVES_MAJEURES = 'Accepté sous réserves majeures'
    
    
    COMMITTE_DECISION_CHOICES = [
        (AVIS_FAVORABLE,'Avis favorable'),
        (ACCEPTE_SOUS_RESERVES_MINEURS,'Accepté sous réserves mineurs'),
        (ACCEPTE_SOUS_RESERVES_MAJEURES,'Accepté sous réserves majeurs'),
        (AVIS_DEFAVORABLE,'Avis défavorable'),
    ] 
    
    
    
    
    
    title = models.CharField(max_length=255, choices=COMMITTE_DECISION_CHOICES)
    description = models.TextField(blank=True)
    
    def __str__(self) -> str:
         return self.title
    
 
class ProjectValidation(models.Model):
    
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='project_to_validate')
    committee = models.ForeignKey(ValidationCommittee, on_delete=models.CASCADE, related_name='project_validation_committe')
    decision = models.ForeignKey(DecisionOfCommittee, on_delete=models.PROTECT, related_name='project_decision') #from the state of this we change the status of the project
    remarques = models.TextField(blank=True)
    validation_date = models.DateField(auto_now=True)
    
    
    def __str__(self) -> str:
         return self.project.project_team.name
    
    
    
######### gestion des recours #########



class Recours(models.Model):
    title = models.CharField(max_length=255)
    date_deposition = models.DateTimeField(auto_now=True)
    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='period_recours')
    
    
    
    def __str__(self) -> str:
         return self.title

   

class RecoursValidation(models.Model):
    recours = models.OneToOneField(Recours, on_delete=models.CASCADE)
    validated_project = models.OneToOneField(ProjectValidation, on_delete=models.CASCADE) 
    
     ### so this one to one field with ProjectValidation insures that we change the decision and the state of the project
     #    it doesn't make sense to do a new relationship with the Project class because first we do ProjectValidation the we do "recours" 
     # so we should into validated project, and change its status, from there we go into the project and change the peride, and wether its rejected , we delete it 
     # all this must be done by one committee so it doesn't make sense to include the committe here because we have it included in the project validation class and its the same
     # we must avoid redendencies 
     # these actions should be handled by the api and we can use signals , but first we should try implementing ModelPermissions(Groups) and see if everything works just fine 
     # but with signals , we can capture them from the sender and perform an action like sending a notification to students that their project has been rejected or acceptes or...etc.
     # note that implementing actions and who perform what and when will be hard, if we couldn't manage to solve the authorization system logique, we could use some libraries that provide
     # model permissions and object level permissions to manage the action due to us having multiple user types, but it would be hard to use these libraries because sometime they cannot 
     # be controlled and throw shocking exceptions so we have complex logic , we must prefearbly implement it from scratch and take the best approaches  
     
    def __str__(self) -> str:
        return self.recours.title