from django.db import models
from django.contrib.auth.models import User

class WasteBin(models.Model):
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    current_fill = models.IntegerField()
    last_collected = models.DateTimeField()
    def __str__(self):
        return self.location

class CollectionSchedule(models.Model):
    bin = models.ForeignKey(WasteBin, on_delete=models.CASCADE)
    collection_time = models.DateTimeField()

class UserReport(models.Model):
    REPORT_TYPES = [
        ('Overflow', 'Overflow'),
        ('Damage', 'Damage'),
        ('Odor Issue', 'Odor Issue'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    photo = models.ImageField(upload_to='report_photos/', blank=True, null=True)
    report_date = models.DateTimeField(auto_now_add=True)
    bin = models.ForeignKey(WasteBin, on_delete=models.CASCADE, related_name='reports')
    report_type = models.CharField(max_length=50, choices=REPORT_TYPES)

    def __str__(self):
        return f"Report by {self.user.username} on {self.report_date}"
class WasteRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bin = models.ForeignKey(WasteBin, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')

class CollectionHistory(models.Model):
    bin = models.ForeignKey(WasteBin, on_delete=models.CASCADE)
    collection_time = models.DateTimeField()
    collected_by = models.CharField(max_length=100)
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()