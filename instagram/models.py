from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

from django.core.validators import MinLengthValidator
# Create your models here.
from django.urls import reverse

# MinValueValidator(10)


class Post(models.Model):
    ip = models.GenericIPAddressField()
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE) 이렇게 하면안댐
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(
        validators=[MinLengthValidator(3, "길이가...")]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m')

    # tag_set = models.ManyToManyField(Tag)
    tag_set = models.ManyToManyField('Tag', blank=True)  # 태그가 없을 수 있다.

    def __str__(self):
        return self.message

    def message_length(self):
        return len(self.message)

    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])


    class Meta:
        ordering = ['-id']
    message_length.short_description = '메세지 글자수'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             limit_choices_to={'is_public': True}) # post_id 필드가 생성된
    # post = models.ForeignKey('instagram.Post', on_delete=models.CASCADE) , 3가지 방법 가능
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50,  unique=True)
    # post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name
