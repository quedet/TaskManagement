from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50, validators=[MinLengthValidator(limit_value=3)])
    due_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title