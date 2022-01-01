from django.db import models

# Create your models here.

class Post(models.Model):
    # All fields are currently manadatory, unless you set them as not.
    title=models.CharField(max_length=200)
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    # User is a built in model that Django provides for authentication
    body=models.TextField()
    
    # Note that in addition to these fields, Django will auto-add a primary key/id field that starts with 1
    
    def __str__(self):
        return self.title
    