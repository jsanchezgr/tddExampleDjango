from django.test import TestCase

from lists.models import Item


class HomePageTests(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_post_request(self):
        response = self.client.post('/', data={'text': 'New'})
        self.assertIn('New', response.content.decode())


class ItemModelTest(TestCase):

    def test_save_retrieve_items(self):
        item_a = Item()
        item_a.text = 'This is the first item'
        item_a.save()

        item_b = Item()
        item_b.text = 'Item the second'
        item_b.save()

        item_list = Item.objects.all()
        self.assertEqual(item_list.count(), 2)

        self.assertEqual(item_list[0].text, 'This is the first item')
        self.assertEqual(item_list[1].text, 'Item the second')