from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Avg, Sum

from grades.models import Grade
from attendance.models import Attendance
from revision.models import RevisionTask
from budget.models import Transaction


@login_required
def dashboard(request):
    # Grades
    grades = Grade.objects.filter(user=request.user)
    avg = grades.aggregate(Avg("score"))["score__avg"] or 0

    # Attendance
    attendance = Attendance.objects.filter(user=request.user)
    total = attendance.count()
    present = attendance.filter(status="present").count()

    percent = 0
    if total > 0:
        percent = (present / total) * 100

    # Revision
    tasks = RevisionTask.objects.filter(
        user=request.user
    ).order_by("date")

    # Budget
    income = Transaction.objects.filter(
        user=request.user,
        type="income"
    ).aggregate(Sum("amount"))["amount__sum"] or 0

    expenses = Transaction.objects.filter(
        user=request.user,
        type="expense"
    ).aggregate(Sum("amount"))["amount__sum"] or 0

    balance = income - expenses

    return render(request, "dashboard/dashboard.html", {
        "grades": grades,
        "avg": round(avg, 2),
        "attendance_percent": round(percent, 1),
        "tasks": tasks,
        "balance": round(balance, 2),
        "income": round(income, 2),
        "expenses": round(expenses, 2),
    })