from django.urls import path
from . views import *


urlpatterns = [
    path('', authenticate, name="authenticate"),
    path('home/', home, name = "home"),
    path('logout/', logout, name = "logout"),
]