from django.db import models

class Note(models.Model):
    name = models.CharField(max_length=100)
    order = models.SlugField()
    text = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return u"Note(%s,%s)" % (self.name, self.order)

    def get_absolute_url(self):
        return u"/note/%s/" % self.order
# Create your models here.
