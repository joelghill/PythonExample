from dataclasses import fields
from django.forms import ModelForm
from django.forms.fields import DateField
from people.models import Person


class PersonForm(ModelForm):

    birthday = DateField(label="Birthday")

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'birthday']

