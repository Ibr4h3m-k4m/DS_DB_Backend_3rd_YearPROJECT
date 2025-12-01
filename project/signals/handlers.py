from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from project.models import Student , Teacher

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_student_for_new_user(sender, **kwargs):
  user = kwargs['instance']    
  if kwargs['created']:
    if user.type == 'Etudiant':
      Student.objects.create(user=user)
      

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_teacher_for_new_user(sender, **kwargs):
  user = kwargs['instance']    
  if kwargs['created']:
    if user.type == 'Enseignant':
      Teacher.objects.create(user=user)