from django import forms
from django.forms import DateTimeField

from tasks.models import Task


class TaskCreateView(forms.ModelForm):
    deadline = DateTimeField(input_formats=["%y-%m-%d"])

    class Meta:
        model = Task
        fields = "__all__"




