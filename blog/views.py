from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


# CBV
class PostList(ListView):
    model = Post
    ordering = '-pk'  # 역순정렬


class PostDetail(DetailView):
    model = Post
    # 템플릿 페이지에서 사용할 데이터 : post


'''
# FBV
def index(requset):
    posts = Post.objects.all().order_by('-pk')
    return render(
        requset,
        'blog/post_list.html',
        {
            'posts': posts,
        }
    )
'''

'''
def detail(requset, pk):
    post = Post.objects.get(pk=pk)
    return render(
        requset,
        'blog/post_detail.html',
        {'post': post},
    )
'''
