from django.shortcuts import render, redirect
from authent.forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model


from authent.models import User


# User = get_user_model()

# def get_user_by_email(email):
#     try:
#         user = User.objects.all()
#         return user
#     except User.DoesNotExist:
#         return None

def registerView(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            # print(new_user)
            username =form.cleaned_data.get('username')
            # print(username)
            messages.success(request, f"Hey {username}, welcome to PayJay!")
            new_user = authenticate(username=form.cleaned_data['email'], password = form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("core:index")
        
    elif request.user.is_authenticated:
        return redirect("core:index")
    form = UserRegistrationForm()      
    context = {
        'form':form
    }
    return render(request, 'authent/register.html', context)

def signInView(request):
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)
        try:
            user = User.objects.get(email=email)
            # password = User.objects.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("core:index")
            else :
                messages.warning(request, "User does not exist")
                return redirect("authUser:sign-in")
        except user.DoesNotExist:
            messages.warning(request, "User does not exist or something")
    return render(request, "authent/login.html")


def logoutView(request):
    logout(request)
    messages.success(request, "Looged Out successfully")
    return redirect("authUser:sign-in")
 


# Create your views here.
