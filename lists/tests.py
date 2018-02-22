from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class HomePageTests(TestCase):

    def test_root_url_resolves_to_homepage(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)