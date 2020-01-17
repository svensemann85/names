from django.db import models

# class Name(models.Model):
#     name = models.CharField(max_length=20)
#     boy = models.BooleanField(default=True)
#     user = models.EmailField()
#     comment = models.CharField(max_length=300)
#     created_at = models.DateTimeField(auto_now_add=True)

class Name(models.Model):
    name = models.CharField(max_length=20)
    boy = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'boy'], name='Name, Sex Unique Constraint')
        ]

class Rating(models.Model):
    fk_name = models.ForeignKey(Name, related_name='ratings', on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    comment = models.CharField(max_length=300, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
