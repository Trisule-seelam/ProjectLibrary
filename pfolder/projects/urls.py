from django.contrib import admin 
from django.urls import path
from projects import views  
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path("",views.home, name='home'),
    path("projects",views.projects, name='projects'),
    path("Contact",views.contacts, name='contacts')

    # path("search",views.search, name='contacts')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

