from django import forms

from ars.subjects.models import Subject

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