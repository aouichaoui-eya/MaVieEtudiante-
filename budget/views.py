from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction


@login_required
def add_transaction(request):
    if request.method == "POST":
        title = request.POST["title"]
        amount = request.POST["amount"]
        ttype = request.POST["type"]
        category = request.POST["category"]

        Transaction.objects.create(
            user=request.user,
            title=title,
            amount=amount,
            type=ttype,
            category=category,
        )

        return redirect("dashboard:dashboard")

    return render(request, "budget/add_transaction.html")