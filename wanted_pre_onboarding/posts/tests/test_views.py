from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class TestProduct(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username = 'jsuh',
            email = 'jsuh@gamil.com',
            password = 'secret',
        )

    def test_get_product_page(self):
        url = reverse('posts:product_create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/product_create.html')

    def test_post_product_create_login(self):
        login = self.client.login(username='jsuh', password='secret')
        self.assertTrue(login)

        url = reverse('posts:product_create')
        response = self.client.post(
            url
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/index.html')
    
    def test_post_product_create_not_login(self):
        url = reverse('posts:product_create')
        response = self.client.post(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/main.html')