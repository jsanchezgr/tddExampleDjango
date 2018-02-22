from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class HomePageTests(TestCase):

    def test_root_url_resolves_to_homepage(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)

    def test_homepage_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Lists</title>', html)
        self.assertTrue(html.endswith('</html>'))