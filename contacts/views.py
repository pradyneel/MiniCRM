from django.shortcuts import render, redirect
from . models import Contacts
from main.models import User

#View Contacts
def contacts(request):
    if request.session.get('user_id', None):
        if request.method == "GET":
            user_id = request.session['user_id']
            user = User.objects.get(id = user_id)
            contact = Contacts.objects.all().filter(user_id = user_id)
            
            context = {
                "contacts" :  contact,
                "user" : user, 
            }
            search_input = request.GET.get('search-area') or ''
            if search_input:
                context["contacts"] = Contacts.objects.all().filter(Name = search_input.lower())

            return render(request, "contacts/contacts.html", context)
    else:
        context = {'message' : 'Login to View the Home Page' , 'class' : 'danger' }
        return redirect('authenticate')

#Add New Contact
def addContact(request):
    if request.session.get('user_id', None):
        if request.method == "POST":
            user_id = request.session['user_id']
            
            Name = request.POST.get('name')
            Company = request.POST.get('company')
            Role = request.POST.get('role')
            PhoneNumber = request.POST.get('phonenumber')
            Email = request.POST.get('email')

            newContact = Contacts(Name = Name.lower(), Company = Company.lower(), Role = Role, PhoneNumber = PhoneNumber, Email = Email.lower(), user_id = user_id)
            newContact.save()
            return redirect('contacts')
        else:
            user_id = request.session['user_id']
            user = User.objects.get(id = user_id)

            context = {
                "user" : user, 
            }
            return render(request, "contacts/addcontacts.html", context)
    else:
        context = {'message' : 'Login to View the Home Page' , 'class' : 'danger' }
        return redirect('authenticate')


       