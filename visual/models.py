from django.db import models

# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True) 

    def __str__(self):
        return format(self.name)

class Tutorial(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True) 
    date = models.DateField(auto_now_add=True, blank=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    def __str__(self):
        return format(self.theme) + ' : ' + format(self.name)