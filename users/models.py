from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    groups = models.ManyToManyField(
        Group,
        related_name='userprofile_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='userprofile_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
class BodyMeasurement(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField()  # in kg
    height = models.FloatField()  # in cm
    shoulders = models.FloatField()  # in cm
    chest = models.FloatField()  # in cm
    waist = models.FloatField()  # in cm
    biceps = models.FloatField()  # in cm
    forearm = models.FloatField()  # in cm
    glutes = models.FloatField()  # in cm

    def __str__(self):
        return f"{self.user.username} - {self.date}"

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    muscle_group = models.CharField(max_length=100)
    image = models.ImageField(upload_to='exercises/', blank=True, null=True)

    def __str__(self):
        return self.name
class Nutrition(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='nutrition/', blank=True)

    def __str__(self):
        return self.name
class Encyclopedia(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='encyclopedia/', blank=True)

    def __str__(self):
        return self.title