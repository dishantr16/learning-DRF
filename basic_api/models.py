from django.db import models

# Create your models here.
Grade = [
    ('excellent', 1),
    ('average', 0),
    ('bad', -1)
]

class DPost(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    uploaded = models.DateTimeField(auto_now_add=True)
    ratings = models.CharField(choices=Grade,default='average',max_length=50)

    class Meta:
        ordering = ['uploaded']

    def __str__(self):
        return self.name