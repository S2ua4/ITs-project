from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("common:login")
    else:
        form = SignupForm()
    return render(request, "common/signup.html", {"form": form})
