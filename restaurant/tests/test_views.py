from django.contrib.auth.models import User
from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a test user and authenticate the client
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create some menu items for testing
        Menu.objects.create(name="Burger", price=50, inventory=30)
        Menu.objects.create(name="Pizza", price=100, inventory=20)

    def test_getall(self):
        response = self.client.get(reverse('menu_items'))
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
