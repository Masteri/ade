from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=128, null=False,blank=True, unique=True)
    categoriya = models.TextField(max_length=200, null=False, blank=True)
    image = models.TextField(max_length=500, null=False, blank=True)
    images = models.TextField(max_length=5000, null=False, blank=True)
    autor = models.TextField(max_length=128, null=False, blank=True)
    datapost = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    #language = models.CharField(choices=LANGUAGE_)
    zmist = models.TextField(max_length=10000, null=False, blank=True)
    def get_absolute_url(self):
        return "/news/%i/" % self.pk

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('created',)