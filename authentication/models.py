from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    class Type(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        NORMAL = "NORMAL", "Normal"
    
    base_type = Type.ADMIN
    
    type = models.CharField(max_length=30, choices=Type.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = self.base_type
            return super().save(*args, **kwargs)

class NormalUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=User.Type.NORMAL)

class NormalUser(User):

    base_type = User.Type.NORMAL

    normal_user = NormalUserManager()

    class meta:
        proxy = True

# @receiver(post_save, sender=NormalUser)
# def create_normal_user_profile(sender, instance, created, **kwargs):
#     if created and instance.type == "NORMAL":
#         NormalUserProfile.objects.create(user=instance)

class NormalUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, default="")
    is_male = models.BooleanField(default=True)
    birth_date = models.DateField(default="1990-01-01")
    job = models.CharField(max_length=50, default="Unemployed")
    description = models.TextField()