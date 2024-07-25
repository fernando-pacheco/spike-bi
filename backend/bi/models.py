from django.db import models
import uuid

class FakeUser(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    salary = models.FloatField()
    job_title = models.CharField(max_length=50)
    age = models.IntegerField()
    company = models.CharField(max_length=50)