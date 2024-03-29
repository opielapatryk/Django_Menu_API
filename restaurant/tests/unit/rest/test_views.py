from django.test import TestCase
from django.test.client import RequestFactory
from rest.views import dish_list
from rest.views import dish_get
from rest.views import dish_post
from rest.views import dish_put
from rest.views import dish_delete
import json
from domain.dish import Dish

class DishListViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_dish_list_view(self):
        # Create a mock request
        request = self.factory.get('/dishes/')

        # Mock repository with test data
        test_dishes = [
            {'id': 1, 'name': 'pizza', 'description': 'italy', 'price': 10.99},
            {'id': 2, 'name': 'burger', 'description': 'american', 'price': 7.99},
            {'id': 3, 'name': 'spaghetti', 'description': 'italy', 'price': 5.99},
            {'id': 4, 'name': 'fries', 'description': 'american', 'price': 1.99}
        ]

        # Call the view function
        response = dish_list(request)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check response content
        expected_content = json.dumps(test_dishes)
        self.assertEqual(response.content.decode('utf-8'), expected_content)

    def test_dish_get_view(self):
        # Create a mock request
        request = self.factory.get('/dishes/3')

        # Mock repository with test data
        test_dish = [
            {'id': 3, 'name': 'spaghetti', 'description': 'italy', 'price': 5.99}
        ]

        # Call the view function
        response = dish_get(request, 3)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check response content
        expected_content = json.dumps(test_dish)
        self.assertEqual(response.content.decode('utf-8'), expected_content)


    def test_dish_post_view(self):
        # Define new dish data
        new_dish_data = {
            'id': 5,
            'name': 'New Dish',
            'description': 'Test description',
            'price': 9.99
        }

        # Send POST request to create a new dish
        request = self.factory.post('/dishes/create/', data=json.dumps(new_dish_data), content_type='application/json')


        response = dish_post(request)

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        domain_dishes = [
                Dish(
                    id=1,
                    name='pizza',
                    description='italy',
                    price=10.99
                ),
                Dish(
                    id=2,
                    name='burger',
                    description='american',
                    price=7.99
                ),
                Dish(
                    id=3,
                    name='spaghetti',
                    description='italy',
                    price=5.99,
                ),
                Dish(
                    id=4,
                    name='fries',
                    description='american',
                    price=1.99
                )
        ]


        expected_response = [dish.to_dict() for dish in domain_dishes + [Dish(**new_dish_data)]]

        response_data = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response_data, expected_response)

    def test_dish_put_view(self):
        # Define new dish data
        update_dish_data = {
            'id': 4,
            'name': 'New Dish',
            'description': 'Test description',
            'price': 9.99
        }

        # Send POST request to create a new dish
        request = self.factory.put('/dishes/update/', data=json.dumps(update_dish_data), content_type='application/json')


        response = dish_put(request)

        self.assertEqual(response.status_code, 200)

        domain_dishes = [
                Dish(
                    id=1,
                    name='pizza',
                    description='italy',
                    price=10.99
                ),
                Dish(
                    id=2,
                    name='burger',
                    description='american',
                    price=7.99
                ),
                Dish(
                    id=3,
                    name='spaghetti',
                    description='italy',
                    price=5.99,
                ),
                Dish(
                    id=4,
                    name='New Dish',
                    description='Test description',
                    price=9.99
                ),
                Dish(
                    id=5,
                    name='New Dish',
                    description='Test description',
                    price=9.99
                )
        ]


        expected_response = [dish.to_dict() for dish in domain_dishes]

        response_data = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response_data, expected_response)

    def test_dish_delete_view(self):
        # Send POST request to create a new dish
        request = self.factory.delete('/dishes/5/delete/', content_type='application/json')

        response = dish_delete(request, 5)

        self.assertEqual(response.status_code, 200)

        domain_dishes = [
                Dish(
                    id=1,
                    name='pizza',
                    description='italy',
                    price=10.99
                ),
                Dish(
                    id=2,
                    name='burger',
                    description='american',
                    price=7.99
                ),
                Dish(
                    id=3,
                    name='spaghetti',
                    description='italy',
                    price=5.99,
                ),
                Dish(
                    id=4,
                    name='fries',
                    description='american',
                    price=1.99
                )
        ]


        expected_response = [dish.to_dict() for dish in domain_dishes]

        response_data = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response_data, expected_response)
