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
    type = models.CharField(max_length = 40)
    description = HTMLField()
    transaction_id = models.CharField(max_length = 500)
    screenshot = models.ImageField(upload_to = 'references/')