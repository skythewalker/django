from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class MiniAppCategory(models.Model):
    APP_TYPE_CHOICE = [
        ('AWS', 'AMAZON WEB SERVICE'),
        ('GCP', 'GOOGLE CLOUD PLATFORM'),
        ('MSA', 'MICROSOFT AZURE'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='minis/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=APP_TYPE_CHOICE)
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name
    
#one to many
class MiniAppReview(models.Model):
    app = models.ForeignKey(MiniAppCategory, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.app.name}'
    
#many to many
class Organization(models.Model):
    ORG_LOCATION = [
        ('ONP', 'ON-PREMISE'),
        ('OFP', 'OFF-PREMISE')
    ]
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, choices=ORG_LOCATION)
    app_varieties = models.ManyToManyField(MiniAppCategory, related_name='organiation')
    
    def __str__(self):
        return self.name

#one to one
class UserProfile(models.Model):
    user = models.OneToOneField(Organization, on_delete=models.CASCADE, related_name='profile')
    user_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    issued_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'User profile for {self.user_name}'