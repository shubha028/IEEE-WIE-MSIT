from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class newNGO(models.Model):
    NGOname = models.CharField(max_length=200, default='')
    Location = models.CharField(max_length=5000,default='')
    PhoneNumber = models.IntegerField(default=0)
    NgoLogo = models.ImageField(default='', upload_to="../media")
    website = models.CharField(max_length=200, default='')
    emailid = models.EmailField(default='xyz@xyz.com')
    VerificationImage = models.ImageField(default='', upload_to="../media")
    Cause = models.CharField(max_length=5000, default='')

    def __str__(self):
        return self.NGOname