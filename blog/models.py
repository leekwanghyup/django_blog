from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # ImageField를 사용하려면 Pillow 라이브러리를 설치해야한다.
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d',blank=True)

    def __str__(self):
        return f'제목 :[{self.pk}] {self.title}'


    def get_url(self):
        return f'/blog/{self.pk}'