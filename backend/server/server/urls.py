from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from mlearn import views

from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mlearn.urls')),
    path('',views.home, name='home'),
]

urlpatterns += endpoints_urlpatterns
