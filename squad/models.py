
from django.db import models

class SquadMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    pet_name = models.CharField(max_length=100)
    traits = models.TextField()
    movie_dialogue = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    video = models.URLField(blank=True)

    def __str__(self):
        return self.name
