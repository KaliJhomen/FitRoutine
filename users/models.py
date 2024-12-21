from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import uuid
class UserProfile(AbstractUser):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    
    weight = models.FloatField(null=True, blank=True)  # Peso en kg
    height = models.FloatField(null=True, blank=True)  # Altura en cm
    shoulders = models.FloatField(null=True, blank=True)  # Hombros en cm
    chest = models.FloatField(null=True, blank=True)  # Pecho en cm
    waist = models.FloatField(null=True, blank=True)  # Cintura en cm
    biceps = models.FloatField(null=True, blank=True)  # Bíceps en cm
    forearm = models.FloatField(null=True, blank=True)  # Antebrazo en cm
    glutes = models.FloatField(null=True, blank=True)  # Glúteos en cm

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
    weight = models.FloatField(null=True)  # in kg
    height = models.FloatField(null=True)  # in cm
    shoulders = models.FloatField(null=True)  # in cm
    chest = models.FloatField(null=True)  # in cm
    waist = models.FloatField(null=True)  # in cm
    biceps = models.FloatField(null=True)  # in cm
    forearm = models.FloatField(null=True)  # in cm
    glutes = models.FloatField(null=True)  # in cm

    def __str__(self):
        return f"{self.user.username} - {self.date}"

