from django.db import models

# Create your models here

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects')

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
