# import_forms
from django import forms
# import Models
from first_app.models import StudentModel
class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentModel
        fields = '__all__'
        # fields = ['name', 'roll']
        # exclude = ['roll']
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll'
        }
        widgets = {
            'name': forms.TextInput(),
        }
        help_texts = {
            'name': "write your full name"
        }
        error_messages = {
            'name': {'required': 'your name is required'}
        } 










