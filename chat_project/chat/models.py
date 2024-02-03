from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
