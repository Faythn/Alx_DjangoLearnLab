from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            request.user.email = email
            request.user.save()  # <-- save() must appear
            return redirect("profile")

    return render(request, "blog/profile.html")
