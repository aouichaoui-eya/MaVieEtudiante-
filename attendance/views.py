from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Attendance

@login_required
def mark_attendance(request):
    if request.method == "POST":
        status = request.POST['status']

        Attendance.objects.create(
            user=request.user,
            status=status
        )

        return redirect('dashboard:dashboard')

    return render(request, "attendance/mark.html")