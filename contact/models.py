from django.db import models


# Create your models here.

class ContactMessages(models.Model):
    name = models.CharField(max_length=200,  null=True)

    email = models.EmailField(max_length=200, null=True, )
    subject = models.CharField(max_length=200,  null=True)
    message = models.TextField(null=True )
    date_added = models.DateTimeField(auto_now_add=True)
