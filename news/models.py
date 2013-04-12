from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title