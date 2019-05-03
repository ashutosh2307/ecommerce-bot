from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactFrom, LoginForm, RegisterForm

def home_page(request):
    context = {
        "title": "Hello World",
        "content": "welcome home"
    }
    if request.user.is_authenticated():
        context["premium_content"] = "Premium"
    return render(request, 'homepage.html', context)

def contact(request):
    contact_form = ContactFrom(request.POST or None)
    context = {
        "title": "contact",
        "content": "welcome contact",
        "form": contact_form, 
        "brand": "new Brand Name"
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, 'contact/view.html', context)

def about(request):
    context = {
        "title": "about",
        "content": "welcome about"
    }
    return render(request, 'homepage.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("user logged in -")
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        # username = request.POST['username']
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(request.user.is_authenticated())
            login(request, user)
            # Redirect to a success page.
            context['form'] = LoginForm()
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            print('not authoried user')
    return render(request, "auth/login.html", context)

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    # print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")

        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)