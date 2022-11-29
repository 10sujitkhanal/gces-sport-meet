from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from sports.models import Batch
from players.models import Player
from core.models import Student

        
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="user_profile")
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.user.username
        
def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        print(instance)
        email = instance.email[0:8]
        batch = Batch.objects.get(batch_name=email)
        name = instance.first_name + " " + instance.last_name
        student = Student.objects.create(student_name=name, batch_name=batch, user=instance)
        userprofile = UserProfile.objects.create(user=instance, batch=batch)
        


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)