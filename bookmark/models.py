from django.db import models

# Create your models here.

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('site URL')

    class Meta:
        ordering = ['site_name']

    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('bookmark:detail', args=[str(self.id)])