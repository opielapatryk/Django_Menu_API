from django.test import TestCase
from django.test.client import RequestFactory
from rest.views import dish_list
import json

class DishListViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_dish_list_view(self):
        # Create a mock request
        request = self.factory.get('/dishes/')

        # Mock repository with test data
        test_dishes = [
            {"id": 1, "name": "pizza", "description": "italy", "price": 10.99},
            {"id": 2, "name": "burger", "description": "american", "price": 7.99},
            {"id": 3, "name": "spaghetti", "description": "italy", "price": 5.99},
            {"id": 4, "name": "fries", "description": "american", "price": 1.99}
        ]

        # Call the view function
        response = dish_list(request)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check response content
        expected_content = json.dumps(test_dishes)
        self.assertEqual(response.content.decode('utf-8'), expected_content)
