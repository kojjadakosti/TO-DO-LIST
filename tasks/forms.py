from django import forms

from tasks.models import Task


class TaskCreationForm(forms.ModelForm):
    task_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    is_completed = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)

    class Meta:
        model = Task
        fields = ('task_name', 'description', 'is_completed')
