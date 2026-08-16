from django.db import models
from employees.models import Employee


class Document(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='documents'
    )

    title = models.CharField(max_length=200)

    file = models.FileField(upload_to='documents/')

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
