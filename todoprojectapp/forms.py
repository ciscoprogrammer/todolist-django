from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'is_completed']

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'name-input'}),
        max_length=255
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'description-input'}),
        required=False  
    )

    is_completed = forms.BooleanField(
        required=False,  
        widget=forms.CheckboxInput(attrs={'class': 'is-completed-input'})
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name

    
