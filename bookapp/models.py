from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=250)
    img=models.ImageField(upload_to='gallery')
    author=models.CharField(max_length=150)
    desc=models.TextField()
    published_year=models.IntegerField()


    def __str__(self):
        return self.title