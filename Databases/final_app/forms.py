from django import forms
from django.contrib.auth.models import User
from .models import Classes, Instructor

class ClassForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ['class_name', 'instructor', 'schedule', 'max_capacity']