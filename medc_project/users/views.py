from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def user_login(request):
    # Like before, obtain the context for the user's request.
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/medc/base') # WHEREVER WE'RE GONNA SEND THEM
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Su cuenta ha sido desactivada.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Usuario o contrasena no invalidos.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, "users/login.html", {})

'''
Function that logs the user out
'''


#@login_required(LOGIN_URL='/users/login/')
def user_logout(request):
    # Since we know the user is lloged in, we can now log them out
    logout(request)
    # Take the user back to login screen
    return HttpResponseRedirect("users/login.html")
