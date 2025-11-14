from django import forms
from .models import Developer, Project


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['first_name', 'last_name', 'email', 'age']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and age < 18:
            raise forms.ValidationError("Developer must be at least 18 years old!")
        return age
        
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if (not first_name) or (not last_name):
            raise forms.ValidationError("Firstname and lastname must be filled!")
        

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'developer']

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise forms.validationError("Description must be filled!")
        return description