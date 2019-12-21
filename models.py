from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=20)
    boy = models.BooleanField(default=True)
    user = models.EmailField()
    comment = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
