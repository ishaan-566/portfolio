from django.db import models
    
    
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.ManyToManyField('Category', related_name="technology")
    date = models.CharField(max_length=20, default='jkl')
    image = models.ImageField(upload_to='project/')
    video = models.TextField(blank=True)
    git = models.TextField(blank=True)
    slide = models.TextField(blank=True)
    document = models.TextField(blank=True)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author)
    
class Certificate(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)

class Language(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.name)
    