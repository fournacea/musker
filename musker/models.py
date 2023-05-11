from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.                                                    #

# Create a User Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follow = models.ManyToManyField(
        "self", 
        related_name="followed_by",
        symmetrical=False,
        blank=True
        ) 

    date_modified = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return f"{self.user.username}"    


# Create Profile when new User signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # User automatically follows themselves
        user_profile.follow.set([instance.profile.id])


post_save.connect(create_profile, sender=User)