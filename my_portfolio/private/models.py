from django.db import models

class Vcard(models.Model):
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15, blank=True)
    front = models.ImageField(upload_to='project/vcards')
    back = models.ImageField(upload_to='project/vcards', blank=True)

    def __str__(self):
        return str(self.title)
