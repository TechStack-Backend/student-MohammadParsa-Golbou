from django.db import models

class Developer(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.last_name


class Project(models.Model):
    title = models.CharField(max_length = 150)
    description = models.CharField(max_length = 300)
    developer = models.ManyToManyField(Developer)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length = 150)
    description = models.CharField(max_length = 300)
    developer = models.ForeignKey(Developer, on_delete = models.CASCADE)

    def __str__(self):
        return self.title