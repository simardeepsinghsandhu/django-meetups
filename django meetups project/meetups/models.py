from django.db import models

# Create your models here.

#one to many relation: one location can have multiple meetups but one meetup will have one location
class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'

#many to many relation
class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True, null=True)
    organizer_email = models.EmailField()
    date = models.DateField()
    
    def __str__(self):
        return f'{self.title}-{self.slug}'