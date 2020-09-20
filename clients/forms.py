from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.Textarea()
    class Meta:
        model = Comment
        fields= [ 'comment']


