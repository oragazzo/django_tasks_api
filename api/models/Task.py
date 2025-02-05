from django.db import models

class Task(models.Model):

    task = models.TextField(null=True)
    completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tasks"
        ordering = ['created_at']

    def __str__(self):
        return self.task