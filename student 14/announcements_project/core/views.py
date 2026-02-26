from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate

# login function allows us to log in a user programmatically
# Note: This can be a bit confusing, but the login function does not authenticate the user, it just logs them in.
# authenticate function allows us to authenticate a user programmatically this tests the username and password against the database.

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after register
            # we implemented the announcement lists let's redirect there after registration
            return redirect("announcement_list")
            # note on the above that it's using the name of the url pattern from announcements/urls.py
            # just another note here, right before the redirect we could also
            # send a welcome email or perform other actions.
    else:
        form = UserRegistrationForm()
    return render(request, "core/register.html", {"form": form})