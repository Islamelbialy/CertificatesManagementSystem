from django.urls import path
from .views import *

urlpatterns = [
    path('newCertificateSettings/', NewCertificateSettings.as_view(), name='newCertificateSettings'),
    path('certificatesTypesForNewCertificateSettings/', certificatesTypesForNewCertificateSettings.as_view(), name='certificatesTypesForNewCertificateSettings'),
]