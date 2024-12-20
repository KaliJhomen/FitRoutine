from django.db import models

class Exercise(models.Model):
    MUSCLE_GROUP_CHOICES = [
        ('pecho', 'Pecho'),
        ('espalda', 'Espalda'),
        ('pierna', 'Pierna'),
        ('brazo', 'Brazo'),
        ('hombro', 'Hombro'),
        ('abdomen', 'Abdomen'),]
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_group = models.CharField(max_length=50, choices=MUSCLE_GROUP_CHOICES)    
    image = models.ImageField(upload_to='manual/exercises/images', blank=True, null=True)
    video= models.FileField(upload_to='manual/exercises/videos', blank= True, null=True)
    def __str__(self):
        return self.name

class Nutrition(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='nutrition/', blank=True, null=True)

    def __str__(self):
        return self.title

class Manual(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    image = models.ImageField(upload_to='manual/', blank=True, null=True)

    def __str__(self):
        return self.question