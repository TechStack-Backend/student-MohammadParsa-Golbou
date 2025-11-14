from django import forms
from .models import Developer, Project

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['first_name', 'last_name', 'email', 'age']

class ProjectForm(forms.ModelForm):
    developer = forms.ModelMultipleChoiceField(
        queryset = Developer.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Project
        fields = ['title', 'description', 'developer']