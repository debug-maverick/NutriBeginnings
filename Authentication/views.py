from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm, RegisterForm, UserForm

# ==========================================
# REGISTER
# ==========================================

def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            # Create the User
            user = form.save()

            # Login the new user
            login(request, user)

            # Go to home
            return redirect('client:home')

    else:

        form = RegisterForm()

    return render(
        request,
        'authentication/register.html',
        {
            'form': form
        }
    )


# ==========================================
# LOGIN
# ==========================================

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check username and password
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            # Login successful
            login(request, user)

            return redirect('client:home')

        else:

            # Login failed
            return render(
                request,
                'authentication/login.html',
                {
                    'error':
                        'Invalid username or password.'
                }
            )

    return render(
        request,
        'authentication/login.html'
    )


# ==========================================
# LOGOUT
# ==========================================

def logout_view(request):

    logout(request)

    return redirect('client:home')

@login_required
def records(request):

    profile = request.user.profile

    if request.method == 'POST':
       #----------------------------------- 
       #this block is only for debugging purposes, to see if the forms are valid and if there are any errors
        print("FORM SUBMITTED")

        user_form = UserForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileForm(
            request.POST,
            instance=request.user.profile
        )

        print("User Form Valid:", user_form.is_valid())
        print("Profile Form Valid:", profile_form.is_valid())

        print("User Form Errors:", user_form.errors)
        print("Profile Form Errors:", profile_form.errors)

        #-------------------

        user_form = UserForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileForm(
            request.POST,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()

            print("USING NEW REDIRECT")
            return redirect('client:home')

    else:

        user_form = UserForm(
            instance=request.user
        )

        profile_form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        'authentication/records.html',
        {
            'user_form': user_form,
            'profile_form': profile_form
        }
    )