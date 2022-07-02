from django.shortcuts import render, redirect
from . models import *
from . sendmail import *
from main.models import User

# Message View
def message(request):
    if request.session.get('user_id', None):
        if request.method == "POST":
            user_id = request.session['user_id']
            receiver_address = request.POST.get('email')
            subject = request.POST.get('text')
            mail_content = request.POST.get('message')

            sendmails(receiver_address, subject, mail_content)
            return redirect('message')
            
        if request.method == "GET":
            user_id = request.session['user_id']
            user = User.objects.get(id = user_id)

            context = {
                "user" : user, 
            }

            return render(request, "message/message.html", context)
        
    else:
        context = {'message' : 'Login to View the Home Page' , 'class' : 'danger' }
        return redirect('authenticate')
    

