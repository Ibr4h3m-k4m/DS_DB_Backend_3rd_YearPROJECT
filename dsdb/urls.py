from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = 'DSDB Admin'
admin.site.index_title = 'DSDB Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include('project.urls')),
    #path('api-auth/', include('rest_framework.urls')),
    #path('rest-auth/', include('rest_auth.urls')),
    #path('rest-auth/registration/', include('rest_auth.registration.urls')),
    #path('api/', include('core.urls', namespace='api')),
    path('__debug__/', include('debug_toolbar.urls')),
] 

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
