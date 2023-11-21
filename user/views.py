from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm

def authentication(request):
    registration_form = RegistrationForm()
    login_form = LoginForm()

    # Handle registration and login forms
    if request.method == 'POST':
        if 'register' in request.POST:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user = registration_form.save(commit=False)
                user.set_password(registration_form.cleaned_data['password'])
                user.save()
                login(request, user)
                return redirect('user:userhome') # Redirect to the user profile page or any other page

        elif 'login' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data['email']
                password = login_form.cleaned_data['password']
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('user:userhome')  # Redirect to the user profile page or any other page
                else:
                    # Display error message using Django messages framework
                     messages.error(request, 'Invalid email or password. Please try again.')
    return render(request, 'authentication.html', {'registration_form': registration_form, 'login_form': login_form})
def userhome(request):
    return render(request, 'user_home.html', {'user': request.user})