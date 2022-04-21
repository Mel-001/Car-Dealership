from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user_profile = models.OneToOneField(User, related_name='currentuser', on_delete=models.CASCADE)
    bio = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.user_profile.username