from django.contrib import admin
from django.utils.html import format_html, urlencode
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from . import models


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email",
                            )}),
        (
            ("Permissions"),
            {
                "fields": (
                    "type",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('type', 'username',
                       'password1', 'password2',
                       'email', 'first_name', 'last_name',),
        }),
    )
    
    list_filter = ('is_staff', 'is_superuser', 'type', 'groups')
    list_display = ('username', 'email', 'first_name', 'type', 'is_staff', 'is_active')
    list_editable = ('is_active', 'is_staff')
    

"""
class StudentInline(admin.StackedInline):
    autocomplete_fields = ['featured_project']
    min_num = 1
    max_num = 6
    model = models.User
    verbose_name = ('Student')
    verbose_name_plural = ('Students')
    
    can_delete = False
    extra = 0

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        
        (("Project info"), {"fields": ("title","establishment", "project_type", "status",
                                        "trademark_name", "scientific_product_name",
                                         "description",
                                        )}),
        (
            ("Project personnel"),
            {
                "fields": (
                    "project_leader",
                    "supervisor",
                    "co_supervisor",
                    "participant",
                ),
            },
        ),
    
        (("Important dates"), {"fields": ("deadline",)}),
    )
    autocomplete_fields = ['project_leader', 'supervisor', 'co_supervisor', 'participant']
    list_display = ['title','status',
                    'project_leader']
    list_filter = ['status','project_leader', 'establishment']
    list_per_page = 10
    search_fields = ['title','description']
    
"""
   


