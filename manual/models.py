from django.db import models

#grupos musculares
class MuscleGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image= models.ImageField(upload_to='manual/musclegroupsimages', blank=True, null=True)
    def __str__(self):
        return self.name
#ejercicios-grupos musculares
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_groups = models.ManyToManyField(MuscleGroup)    
    image = models.ImageField(upload_to='manual/exercises/images', blank=True, null=True)
    video= models.FileField(upload_to='manual/exercises/videos', blank= True, null=True)
    def __str__(self):
        return self.name
##Suplementos
class Suplements(models.Model):
    name= models.CharField(max_length=50)
    image= models.ImageField(upload_to='manual/suplementsimages', blank=True, null=True)
    def __str__(self):
        return self.name
#suplementos nutricionales - suplementos
class NutritionalSuplements(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    nutritional_suplements= models.ManyToManyField(Suplements)
    image = models.ImageField(upload_to='manual/nutritionalsuplementsimages', blank=True, null=True)
    def __str__(self):
        return self.title
##si hay tiempo...
class Manual(models.Model):
    pass