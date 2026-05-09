from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import RevisionTask


@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        date = request.POST["date"]

        RevisionTask.objects.create(
            user=request.user,
            title=title,
            description=description,
            date=date
        )

        return redirect("dashboard:dashboard")

    return render(request, "revision/add_task.html")


@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(
        RevisionTask,
        id=task_id,
        user=request.user
    )

    task.is_done = not task.is_done
    task.save()

    return redirect("dashboard:dashboard")


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(
        RevisionTask,
        id=task_id,
        user=request.user
    )

    task.delete()

    return redirect("dashboard:dashboard")