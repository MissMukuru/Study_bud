from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#this meaans that the post model and the user model have a realtionship(one to many) because one auther can create multiple users.

#Each class is going to be its own table in the database
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE) #on_delete is used to tell django that we want to delete their post if the user has been deleted as well

    def __str__(self):
        return self.title
