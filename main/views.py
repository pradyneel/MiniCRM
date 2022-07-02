from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import make_password, check_password
import os
    
#Verify email and password
def verify_login(email, password):
    user = User.objects.filter(userEmail = email).first()
 
    #If user doesn't exists
    if user is None:
        return False
    #if user exists 
    else:
        password = check_password(password, user.password)
        if password:
            return True
        else:
            return False


#User Authentication Function
def authenticate(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'Login':
            #get login request input
            email = request.POST.get('email')
            password =  request.POST.get('password')

            #Verify email and password
            if verify_login(email, password):
                user = User.objects.filter(userEmail = email).first()
                request.session['user_id'] = user.id
                return redirect('home')
            
            error = "Incorrect Credentials"
            return render(request, "main/authenticate.html", {"errors" : error})
        
        elif request.POST.get('submit') == 'SignUp':
            #Get user Input
            userEmail = request.POST.get('email')
            userName = request.POST.get('name')
            userCompany = request.POST.get('company')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password1 == password2:
                #Check if the user already exists
                check_user = User.objects.filter(userEmail = userEmail).first()

                #Return existing user message in SignUp 
                if check_user:
                    context = {'message' : 'User already exists' , 'class' : 'danger' }
                    return render(request, 'main/authenticate.html' , context)
                else:
                    #Hash password to store in the DB
                    password = make_password(password1, salt= None, hasher = "default")

                    #save user to the DB
                    user = User(userEmail = userEmail, userName = userName, userCompany = userCompany, password = password)
                    user.save()

                    #Redirecting user to Main/authenticate
                    return redirect('authenticate')
            else:
                context = {'message' : 'Password Mismatch'}
                return render(request, 'main/authenticate.html', context)

    return render(request, 'main/authenticate.html')


#Home page
def home(request):
    if request.session.get('user_id', None):
        user_id = request.session['user_id']
        user = User.objects.get(id = user_id)
        
        context = {
            "user" : user, 
        }

        return render(request, "main/home.html", context)
        
    else:
        context = {'message' : 'Login to View the Home Page' , 'class' : 'danger' }
        return redirect('authenticate')

def logout(request):
    del request.session['user_id']
    
    if os.path.isfile("token_gmail_v1.pickle"):
        os.remove("token_gmail_v1.pickle")
    else:
        print("File doesn't exists")
    return redirect("authenticate")
        
    
