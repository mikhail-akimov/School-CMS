from django import forms
from .models import Grade


class AddGrade(forms.ModelForm):
    name = forms.CharField(help_text="Enter class name")
    model = Grade
    fields = ('name', 'lead')

    def clean_name(self):
        name = self.cleaned_data['name']
        print(name)
        print(name[-1])

        if len(name) > 3:
            raise ValueError('Grade name is too long!')

        elif len(name) < 2:
            raise ValueError('Grade name is too short!')

        elif name[-1].isdigit():
            raise ValueError('Please enter grade char.')

        else:
            return name
