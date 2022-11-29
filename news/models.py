from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from sports.models import Sports
import uuid
from django.contrib.auth.models import User
# Create your models here.
class News(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    sports = models.ForeignKey(Sports, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='images/')
    video = models.CharField(max_length=100, null=True, blank=True)
    detail = RichTextUploadingField()
    is_active = models.BooleanField(default=True)
    post_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="110"/>'.format(self.image.url))

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'uuid': self.uuid})