from django.shortcuts import render, redirect
from authent.forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def registerView(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("amen")
            new_user=form.save()
            # print(new_user)
            username =form.cleaned_data.get('username')
            print(username)
            messages.success(request, f"Hey {username}, welcom to PayJay!")
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

# Create your views here.
