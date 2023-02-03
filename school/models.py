from django.db import models
#from django.core.validators import MinLengthValidator

# Create your models here.

class school_database(models.Model):

    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    subjectName = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    video = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name