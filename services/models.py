import shortuuid
from .choices import *
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Query(models.Model):
    user_name = models.CharField(max_length = 100)
    registration_id = models.CharField(max_length = 200)
    college_name = models.CharField(max_length = 400)
    title = models.CharField(max_length = 30)
    description = HTMLField()
    transaction_id = models.CharField(max_length = 500)
    status = models.CharField(max_length = 100,choices = STATUS_CHOICES,blank = True)
    screenshot = models.ImageField(upload_to = 'references/')
    date_of_creation = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(blank = True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = shortuuid.ShortUUID().random(length=10)
        super(Query, self).save(*args,**kwargs)
    def __str__(self):
        return self.title+"-"+self.user_name+"-"+self.slug