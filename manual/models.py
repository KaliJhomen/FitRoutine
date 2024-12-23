from django.db import models

#grupos musculares
class Muscle(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image= models.ImageField(upload_to='manual/musclesimages', blank=True, null=True)
    def __str__(self):
        return self.name
#tags a usar 
class Tag(models.Model):
    name= models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.name
    
#ejercicios-grupos musculares
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscles = models.ManyToManyField(Muscle)    
    tags= models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='manual/exercises/images', blank=True, null=True)
    video= models.FileField(upload_to='manual/exercises/videos', blank= True, null=True)
    def __str__(self):
        return self.name
##Suplementos
class NutritionalSuplement(models.Model):
    name= models.CharField(max_length=50)
    image= models.ImageField(upload_to='manual/nutritionalsuplementsimages', blank=True, null=True)
    def __str__(self):
        return self.name
#suplementos nutricionales - suplementos
class Suplement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    nutritional_suplement= models.ManyToManyField(NutritionalSuplement)
    image = models.ImageField(upload_to='manual/suplementsimages', blank=True, null=True)
    def __str__(self):
        return self.name
    
##si hay tiempo...
class Manual(models.Model):
    pass