from django import forms
from django.conf import settings
from django.contrib.auth.models import User

from ars.subjects.models import Subject
from ars.core.models import UserProfile

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