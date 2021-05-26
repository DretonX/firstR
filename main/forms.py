from django.forms import ModelForm

from main.models import PersonModel


class PersonForm(ModelForm):
    class Meta:
        model = PersonModel
        fields = ['first_name', 'last_name', 'password', 'email']
