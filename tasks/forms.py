from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags", "is_done"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
            "deadline": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }
