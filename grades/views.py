from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Grade

@login_required
def add_grade(request):
    if request.method == "POST":
        subject = request.POST['subject']
        score = request.POST['score']

        Grade.objects.create(
            user=request.user,
            subject=subject,
            score=score
        )

        return redirect('dashboard:dashboard')

    return render(request, "grades/add_grade.html")