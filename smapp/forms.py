from tkinter.ttk import LabeledScale
from django import forms
from smapp.models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        labels ={
            'name' : "Name",
            'marks' : "Marks",
            'roll_num' : "Roll No",
            
        
        }

class updateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        labels ={
            'name' : "Updated Name",
            'marks' : "Updated Marks",
            'roll_num' : "Updated Roll No",
        
        }

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

