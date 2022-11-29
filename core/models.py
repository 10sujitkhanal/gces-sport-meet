from django.db import models
import uuid
from sports.models import Batch
from django.conf import settings

# Create your models here.

class Student(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    student_name = models.CharField(max_length = 100)
    batch_name = models.ForeignKey(Batch, on_delete = models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)