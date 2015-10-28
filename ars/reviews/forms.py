from django import forms

from .models import Review

class ReviewSubjectForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('rating', 'content')
