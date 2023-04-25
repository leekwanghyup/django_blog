import os.path

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)

    hook_text = models.CharField(max_length=200, blank=True)

    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # ImageField를 사용하려면 Pillow 라이브러리를 설치해야한다.
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank=True)

    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)

    # 작성자가 삭제된 포스트에 작성자란 빈칸으로 남겨 둠
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'제목 :[{self.pk}] {self.title} :: {self.author}'

    def get_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
