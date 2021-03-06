from django import forms
from django.conf import settings
from django.contrib.auth.models import User

from ars.subjects.models import Subject
from ars.core.models import UserProfile
from ars.subjects.models import Task, Session

class SubjectForm(forms.ModelForm):
    """docstring for SubjectForm"""
    class Meta:
        model = Subject
        fields = ('categories', 'course', 'name', 'slug',
                    'description', 'image')

        widgets = {
            'categories': forms.widgets.SelectMultiple(
                attrs={'class': 'form-control select2',
                        'style': 'width: 100%;',
                        'multiple': "multiple"}),

            'course': forms.widgets.Select(
                attrs={'class': 'form-control select2',
                        'style': 'width: 100%;'}),            
        }


class TeacherForm(forms.ModelForm):
    re_password = forms.CharField(max_length=500)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password',)

    def clean(self):
        cleaned_data = super(TeacherForm, self).clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if password != re_password:
            msg = "Password not contrain."
            self.add_error('re_password', msg)


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('session', 'name', 'slug',
                    'content', 'start_date', 'end_date')

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date', False)
        end_date = cleaned_data.get('end_date', False)

        if start_date and end_date and start_date > end_date:
            msg = "'End date' must be later than 'Start date'"
            self.add_error('start_date', msg)
            self.add_error('end_date', msg)

        return cleaned_data


class SessionForm(forms.ModelForm):

    class Meta:
        model = Session
        fields = ('subject', 'start_date', 'end_date')

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date', False)
        end_date = cleaned_data.get('end_date', False)

        if start_date and end_date and start_date > end_date:
            msg = "'End date' must be later than 'Start date'"
            self.add_error('start_date', msg)
            self.add_error('end_date', msg)

        return cleaned_data
