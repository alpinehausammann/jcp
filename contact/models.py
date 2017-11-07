from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length = 255, Required = True)
    phone = models.CharField(max_length = 15, Required = True)
    email = models.EmailField(max_length = 254, Required = True)
    address = models.CharField(max_length = 254, Required = True)
    description = models.TextField()




    def publish(self):
        self.publish_date = timezone.now()
        self.save
