from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()


    def __str__(self):
        return self.title
        
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField("")
    message = models.TextField()
    
    
    def str(self):
        return self.name
