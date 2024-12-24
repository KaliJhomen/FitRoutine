from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import uuid
class UserProfile(AbstractUser):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    groups = models.ManyToManyField(
        Group,
        related_name='userprofile_set',
        blank=True,
        help_text='Los grupos a los que este usuario pertenece.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='userprofile_set',
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='user permissions',
    )
    def __str__(self):
        return f"{self.user.username} - {self.date}"

class BodyMeasurement(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField(null=True, blank=True)  
    height = models.FloatField(null=True, blank=True)  
    shoulders = models.FloatField(null=True, blank=True)  
    chest = models.FloatField(null=True, blank=True)  
    waist = models.FloatField(null=True, blank=True)  
    biceps = models.FloatField(null=True, blank=True)  
    forearm = models.FloatField(null=True, blank=True) 
    glutes = models.FloatField(null=True, blank=True)  
    def __str__(self):
        return f"{self.user.username} - {self.date}"

