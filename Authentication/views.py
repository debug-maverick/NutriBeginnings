from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import RegisterForm

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