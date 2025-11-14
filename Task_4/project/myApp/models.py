from django.db import models
from django.urls import reverse

class Developer(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.last_name
    
    def get_absolute_url(self):
        return reverse('developer_detail', kwargs = {'pk': self.pk})
    

class Project(models.Model):
    title = models.CharField(max_length = 150)
    description = models.CharField(max_length = 300)
    developer = models.ManyToManyField(Developer)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs = {'pk': self.pk})