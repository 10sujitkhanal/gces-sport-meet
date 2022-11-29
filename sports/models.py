from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
import uuid
from django.urls import reverse

# Create your models here.

class Sports(models.Model):
    MULTIPLE = 'MULTIPLE'
    SINGLE = 'SINGLE'
    TYPE_CHOICES = [
        (MULTIPLE, 'MULTIPLE'),
        (SINGLE, 'SINGLE'),
    ]
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    sport_name = models.CharField(max_length=100)
    sport_type = models.CharField(max_length=9,choices=TYPE_CHOICES, default=MULTIPLE)
    icon = models.ImageField(blank=True, upload_to='images/icons')
    image = models.ImageField(blank=True, upload_to='images/sports/images')
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sport_name

class Batch(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    batch_name = models.CharField(max_length=100)
    batch_id = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.batch_name

class Team(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    batch = models.ForeignKey(Batch, on_delete = models.CASCADE)
    team_name = models.CharField(max_length=100)
    contact = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.team_name

class Position(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    position = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position