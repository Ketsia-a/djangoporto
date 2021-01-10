from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
   path('',views.homepage,name = 'homepage'),
   path('location/<location>',views.location,name = 'location'),
   path('search',views.search_image,name = 'search_image')
]
if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

