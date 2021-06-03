from django.db import models
from django.contrib.auth.models  import User
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description =models.TextField(max_length=400)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title