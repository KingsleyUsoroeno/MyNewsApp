from django.urls import path
from .views import fetchJsonData

urlpatterns = [
    path('', fetchJsonData, name='jsonUrl')
]
