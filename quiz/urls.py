from django.urls import path, include
from .views import *

urlpatterns = [path('translate/', translateApi.as_view())]
