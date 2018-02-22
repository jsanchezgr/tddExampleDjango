from django.test import TestCase


class HomePageTests(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_post_request(self):
        response = self.client.post('/', data={'text': 'New'})
        self.assertIn('New', response.content.decode())
