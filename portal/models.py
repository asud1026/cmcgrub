import datetime
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, Textarea
from django import forms
from django.forms.widgets import CheckboxSelectMultiple 
from django.core import exceptions
from django.utils.text import capfirst 

# Side Choices
MAIN_CHOICES = (
        ('Sandwhich', 'Sandwhich'),
        ('Burger', 'Burger'),
    )

SIDE_CHOICES = (
        ('Lettuce', 'Lettuce'),
        ('Tomato', 'Tomato'),
    )

PAYMENT_CHOICES = (
        ('Flex', 'Flex'),
        ('Claremont Cash', 'Claremont Cash'),
    )

# Multiple Selection Form
class MultiSelectFormField(forms.MultipleChoiceField):
    widget = forms.CheckboxSelectMultiple
 
    def __init__(self, *args, **kwargs):
        self.max_choices = kwargs.pop('max_choices', 8)
        super(MultiSelectFormField, self).__init__(*args, **kwargs)
 
    def clean(self, value):
        if not value and self.required:
            raise forms.ValidationError(self.error_messages['required'])
        # if value and self.max_choices and len(value) > self.max_choices:
        #     raise forms.ValidationError('You must select a maximum of %s choice%s.'
        #             % (apnumber(self.max_choices), pluralize(self.max_choices)))
        return value

# Models for the multiple selction form
class MultiSelectField(models.Field):
    __metaclass__ = models.SubfieldBase
 
    def get_internal_type(self):
        return "CharField"
 
    def get_choices_default(self):
        return self.get_choices(include_blank=False)
 
    def _get_FIELD_display(self, field):
        value = getattr(self, field.attname)
        choicedict = dict(field.choices)
 
    def formfield(self, **kwargs):
        # don't call super, as that overrides default widget if it has choices
        defaults = {'required': not self.blank, 'label': capfirst(self.verbose_name),
                    'help_text': self.help_text, 'choices': self.choices}
        if self.has_default():
            defaults['initial'] = self.get_default()
        defaults.update(kwargs)
        return MultiSelectFormField(**defaults)

    def get_prep_value(self, value):
        return value

    def get_db_prep_value(self, value, connection=None, prepared=False):
        if isinstance(value, basestring):
            return value
        elif isinstance(value, list):
            return ",".join(value)
 
    def to_python(self, value):
        if value is not None:
            return value if isinstance(value, list) else value.split(',')
        return ''

    def contribute_to_class(self, cls, name):
        super(MultiSelectField, self).contribute_to_class(cls, name)
        if self.choices:
            func = lambda self, fieldname = name, choicedict = dict(self.choices): ",".join([choicedict.get(value, value) for value in getattr(self, fieldname)])
            setattr(cls, 'get_%s_display' % self.name, func)
 
    def validate(self, value, model_instance):
        arr_choices = self.get_choices_selected(self.get_choices_default())
        #for opt_select in value:
        #    if (int(opt_select) not in arr_choices):  # the int() here is for comparing with integer choices
        #        raise exceptions.ValidationError(self.error_messages['invalid_choice'] % value)  
        return True
 
    def get_choices_selected(self, arr_choices=''):
        if not arr_choices:
            return False
        list = []
        for choice_selected in arr_choices:
            list.append(choice_selected[0])
        return list
 
    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

# The main note model
class Note(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now=True)
    main = MultiSelectField(max_length=250, blank=True, choices=MAIN_CHOICES)
    side =  MultiSelectField(max_length=250, blank=True, choices=SIDE_CHOICES)
    payment = MultiSelectField(max_length=250, blank=True, choices=PAYMENT_CHOICES)
    comments = models.TextField()
    approved = 0;
    def __unicode__(self):
       return self.main
    def save(self, *args, **kwargs):
        return super(Note, self).save(*args, **kwargs)

#The note's modelform
class NoteForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
    #  super(NoteForm, self).__init__(*args, **kwargs)
    #  self.fields['MAIN_CHOICES'].widget = forms.CheckboxSelectMultiple()
    #main = forms.ModelChoiceField(queryset=Note.objects.all(), empty_label='Manual Team Entry:', required=False)
    #def __init__(self, *args, **kwargs):  
          
        #super(CompanyForm, self).__init__(*args, **kwargs)  
          
        #self.fields["side"].widget = CheckboxSelectMultiple()  
        #self.fields["side"].queryset = Industry.objects.all()  

    #main = models.TextField(max_length=1, choices=MAIN_CHOICES, null=True)
    main = MultiSelectFormField(choices=MAIN_CHOICES,
    widget=forms.Select())
    side = MultiSelectFormField(choices=SIDE_CHOICES,
    widget=forms.CheckboxSelectMultiple)
    payment = MultiSelectFormField(choices=PAYMENT_CHOICES,
    widget=forms.Select())
    class Meta:
        model = Note
        fields = ('user','main', 'side', 'payment', 'comments',)












        