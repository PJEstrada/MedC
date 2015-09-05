from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

'''
    Organization: An organization
'''

'''
class Organization(models.Model):
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=True)
    name = models.CharField(max_length=255)


    def __unicode__(slef):
        return self.name

'''
'''
    User Profile that has a one to one relation with User
'''


class ClinicUser(models.Model):
    # Links UserProfile to a User model instance
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    # organization = models.ForeignKey('Organization')
    date_of_birth = models.DateField()
    role = models.IntegerField(default=0)
    mobile_number = models.IntegerField()
    home_number = models.IntegerField()

    def __unicode__(self):
        verbose = self.first_name + self.last_name
        return verbose
