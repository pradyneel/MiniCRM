from django.urls import path
from . views import contacts, addContact

urlpatterns = [
    path('contacts/', contacts, name="contacts"),
    path('addcontact/', addContact, name="addcontact"),
]
