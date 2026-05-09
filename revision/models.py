from django.db import models
from django.contrib.auth.models import User
from datetime import date


class RevisionTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    is_done = models.BooleanField(default=False)

    @property
    def status(self):
        today = date.today()

        if self.is_done:
            return "done"
        elif self.date < today:
            return "overdue"
        elif self.date == today:
            return "today"
        return "upcoming"

    def __str__(self):
        return self.title