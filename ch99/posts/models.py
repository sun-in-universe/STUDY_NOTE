from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from .validators import validate_symbols, validate_no_profanity
from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=50, unique=False, validators=[
        MinLengthValidator(5, "너무 짧아요! 좀 더 길게 적어주세요!"),
        validate_symbols, validate_no_profanity,
    ])
    content = models.TextField(validators=[
        MinLengthValidator(10, "너무 짧아요! 좀 더 길게 적어주세요!"),
        validate_symbols, validate_no_profanity,
    ])
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # ForeignKey를 사용해 Post 모델과 관련짓음
    content = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.post.title}"