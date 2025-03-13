from django import forms

from tasks.models import Task


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_name', 'description', 'date_till_end')
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
