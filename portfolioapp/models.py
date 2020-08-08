from django.db import models
from cloudinary.models import CloudinaryField

class Project(models.Model):
    name = models.CharField(max_length = 30)
    screenshot = CloudinaryField('Project screenshot')
    languages = models.TextField()
    short_description = models.TextField(default="short description")
    long_description = models.TextField(default="long description")
    link = models.URLField()
    post_date = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.name

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    class Meta:
        ordering = ['-post_date']
    
