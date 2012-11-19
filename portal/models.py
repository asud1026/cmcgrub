import datetime
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

#class Note(models.Model):
#    name = models.CharField(max_length=100)
#    order = models.SlugField()
#    text = models.TextField(blank=True,null=True)

#    def __unicode__(self):
#        return u"Note(%s,%s)" % (self.name, self.order)

#    def get_absolute_url(self):
#        return u"/note/%s/" % self.order

class Note(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now=True)
   # title = models.CharField(max_length=200)
   # slug = models.SlugField()
    body = models.TextField()

    #def __unicode__(self):
       # return self.title

    def save(self, *args, **kwargs):
        return super(Note, self).save(*args, **kwargs)

class NoteForm(ModelForm):
    class Meta:
        model = Note
