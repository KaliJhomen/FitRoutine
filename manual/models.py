from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_group = models.CharField(max_length=50)
    image = models.ImageField(upload_to='exercises/', blank=True, null=True)

    def __str__(self):
        return self.name

class Nutrition(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='nutrition/', blank=True, null=True)

    def __str__(self):
        return self.title

class Encyclopedia(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    image = models.ImageField(upload_to='encyclopedia/', blank=True, null=True)

    def __str__(self):
        return self.question