from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework_nested import routers
from . import views



router = routers.DefaultRouter()
router.register('students', views.StudentViewSet, basename='students')
router.register('teachers', views.TeacherViewSet, basename='teachers')
router.register('periods', views.PeriodViewSet)
router.register('etablissement', views.EtablissementViewSet)
##### project deposition
router.register('project-invitations', views.ProjectInvitationViewSet, basename='project-invitations')
router.register('project-teams', views.ProjectTeamViewSet)
router.register('management-teams', views.ManagementTeamViewSet)
router.register('project-types', views.ProjectTypeViewSet)
router.register('projects', views.ProjectViewSet, basename='projects')
#### project Validation
router.register('validation-committees', views.ValidationCommitteeViewSet)
router.register('decision-of-committees', views.DecisionOfCommitteeViewSet)
router.register('project-validations', views.ProjectValidationViewSet)
#### gestion recours
router.register('recours', views.RecoursViewSet)
router.register('recours-validations', views.RecoursValidationViewSet)



urlpatterns = router.urls