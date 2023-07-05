from django.db import models

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%M/%D/")
    time_create = models.DateTimeField(auto_now_add=True) # один раз и не меняется
    time_update = models.DateTimeField(auto_now=True) # меняется
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    