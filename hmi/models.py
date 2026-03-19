from django.db import models

# Create your models here.
class SetPointLog(models.Model):
    # Records the value the user entered
    value = models.FloatField()
    # Automatically records the date and time of the change
    timestamp = models.DateTimeField(auto_now_add=True)
    # Records the status at that time
    status_message = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.timestamp} - {self.value} ({self.status_message})"