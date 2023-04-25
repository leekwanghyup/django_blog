from bs4 import BeautifulSoup
from django.test import TestCase, Client

from blog.models import Post


# Create your tests here.
class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        post_001 = Post.objects.create(
            title='첫 번째 포스트 입니다.',
            content='Hello World. We are teh world'
        )
        post_002 = Post.objects.create(
            title='두 번째 포스트 입니다.',
            content='1등이 전부는 아니잖아요?'
        )

    def test_post_list(self):
        # /blog/로 요청하면 200코드를 반환한다.
        response = self.client.get('/blog/')
        self.assertEquals(response.status_code, 200)

        # 페이지 타이틀이 Blog 이다.
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEquals(soup.title.text, 'Blog')

        # 네비게이션 태그가 존재한다.
        navbar = soup.nav
        self.assertIsNotNone(navbar)
        # self.assertIsNone(navbar)

        # 네이비게이션 태그 내에 Blog, About Me 문구가 포함되어있다.
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)

        # 포스트 게시물이 2개이다.
        self.assertEquals(Post.objects.count(), 2)

        # main area에 '아직 게시물이 없습니다.'라는 문구가 나타난다.
        main_area = soup.find('div',id='main_area')
        self.assertIsNotNone(main_area);
        self.assertIn('아직 게시물이 없습니다.', main_area.text)