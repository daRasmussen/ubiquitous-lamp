from django.contrib.auth.models import User
from django.db import models

"""
    [ ] user_image = 
    [ ] user_phone = 
    [ ] user_address = FK One-To-Many
    [ ] user_comments = FK One-To-many
    [ ] user_items = FK-One-To-Many
"""


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='main/images/profiles')
    phone = models.CharField(max_length=150)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
