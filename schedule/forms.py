from django import forms
from .models import Grade
from django.utils.translation import gettext as _


class AddGrade(forms.ModelForm):
    name = forms.CharField(help_text="Enter class name", max_length=3, min_length=2,
                           error_messages={'required': 'Укажите логин'})

    class Meta:
        model = Grade
        fields = ['name', 'lead']

    def clean_name(self):
        name = self.cleaned_data['name']

        if name[-1].isdigit():
            raise ValueError(_('Please enter grade char.'))
        return name
