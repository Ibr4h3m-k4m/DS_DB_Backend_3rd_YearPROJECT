from django.contrib import admin
from django.utils.html import mark_safe
from django.conf import settings
from django.contrib.auth.models import  AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _




class User(AbstractUser):
    
    STUDENT = 'Etudiant'
    TEACHER = 'Enseignant'
    

    USER_TYPE_CHOICES = [
    (STUDENT,'Etudiant'),
    (TEACHER,'Enseignant'),
    ]
    
                
    email = models.EmailField(unique=True)
    type = models.CharField(_('user type'), help_text=_('Designates whether the user is a student or a teacher.'),
                            max_length=50, choices=USER_TYPE_CHOICES, blank=False,
                            )
   
   
   

    
   
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'type', ]
   
    """
    def picture_preview(self): #new
            return mark_safe(f'<img src = "{self.picture.url}" width="100px" height= "100px" object-fit="cover"/>')
    """  
        



   