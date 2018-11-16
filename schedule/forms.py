from django import forms
from .models import Grade


class AddGrade(forms.ModelForm):
    name = forms.CharField(help_text="Enter class name")

    def clean_grade_name(self):
        name = self.cleaned_data['name']

        if len(name) > 3:
            raise ValueError(_('Grade name is too long!'))

        if len(name) < 2:
            raise ValueError(_('Grade name is too short!'))

        if name[-1] in range(0, 9):
            raise ValueError(_('Please enter grade char.'))

        return name
