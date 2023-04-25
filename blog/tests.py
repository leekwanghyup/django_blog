from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.test import TestCase, Client

from blog.models import Post


# Create your tests here.
class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        # 작성자 생성
        self.user_trump = User.objects.create_user(username='trump', password='smoepassword')
        self.user_obama = User.objects.create_user(username='obama', password='smoepassword')

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

        # 포스트 게시물이 0개이다.
        self.assertEquals(Post.objects.count(), 0)
        post_001 = Post.objects.create(
            title='첫 번째 포스트 입니다.',
            content='Hello World. We are teh world',
            author=self.user_trump
        )
        post_002 = Post.objects.create(
            title='두 번째 포스트 입니다.',
            content='1등이 전부는 아니잖아요?',
            author=self.user_obama
        )

        # 포스트 게시물이 2개이다.
        self.assertEquals(Post.objects.count(), 2)

        # main area에 '아직 게시물이 없습니다.'라는 문구가 나타난다.
        main_area = soup.find('div', id='main_area')
        self.assertIsNotNone(main_area);
        self.assertIn('아직 게시물이 없습니다.', main_area.text)
        self.assertIn(self.user_trump.username.upper(), main_area.text)
        self.assertIn(self.user_obama.username.upper(), main_area.text)

    def test_post_detail(self):
        post_001 = Post.objects.create(
            title='첫 번째 포스트 입니다.',
            content='Hello World. We are teh world'
        )
        # post_001의 url은 '/blog/1' 이다.
        self.assertEquals(post_001.get_url(), '/blog/1/')

        # 첫 번째 포스트의 상세페이지 접근
        response = self.client.get(post_001.get_url())
        self.assertEquals(response.status_code, 200)

        # 네비게이션 바가 존재한다.
        soup = BeautifulSoup(response.content, 'html.parser')
        navbar = soup.nav
        self.assertIsNotNone(navbar)
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)

        # 포스트의 제목이 웹 브라우저 탭 타이틀에 포함되어있다.
        self.assertIn(post_001.title, soup.title.text)

        # 포스트의 제목이 포스트 영역(post_area)에 있다.
        post_area = soup.find('article', id='post-area')
        self.assertIn(post_001.title, post_area.text)

        # 포스트의 내용이 포스팅 영역에 있다.
        self.assertIn(post_001.content, post_area.text)