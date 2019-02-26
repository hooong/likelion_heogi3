from django.db import models

class Clothe(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.title
