from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['tab_number', 'full_name', 'email', 'phone', 'position']