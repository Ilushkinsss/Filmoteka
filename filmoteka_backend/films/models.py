from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()
    director = models.CharField(max_length=50)
    genres = models.ManyToManyField('Genre')


    def __str__(self):
        return self.title


from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    biography = models.TextField()
    actors = models.ManyToManyField('Actor')

    def __str__(self):
        return self.name

# Create your models here.
