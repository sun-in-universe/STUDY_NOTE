from typing import Any
from django import forms
from .models import Post, Comment
from .validators import validate_symbols
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):    
   
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'title',
                'placeholder': '제목을 입력하세요'}),
            'content': forms.Textarea(attrs={
                'placeholder': '내용을 입력하세요'})} 

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title', '')
        if '*' in title:
            raise forms.ValidationError('*는 포함될 수 없습니다.')
        return cleaned_data 
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': '댓글을 입력하세요'})
        }

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content', '')
        if '*' in content:
            raise forms.ValidationError('*는 포함될 수 없습니다.')
        return cleaned_data