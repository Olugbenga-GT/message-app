from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='How about we get fucked up ?')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'How about we get fucked up ?')

class HomePageViewTest(TestCase):
    def SetUp(self):
        Post.objects.create(text='Another one ...')

    def test_that_view_is_at_expected_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_if_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')