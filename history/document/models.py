from django.db import models

# Create your models here.
class Document(models.Model):
    UNIT_CHOICES = [
        ('unit2', 'Unit 2'),
        ('unit3', 'Unit 3'),
        ('unit7', 'Unit 7'),
    ]
    title= models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    author = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    unit = models.CharField(max_length=5, choices=UNIT_CHOICES)
    def __str__(self):
        return self.title