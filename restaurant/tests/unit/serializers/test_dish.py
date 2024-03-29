import json
from domain.dish import Dish
from serializers.dish import DishJsonEncoder

def test_serializer_domain_dish():
    dish = Dish(1,'pizza','italian dish',2.99)

    expected_json = """
        {
        "id": 1,
        "name": "pizza",
        "description": "italian dish",
        "price": 2.99
        }
    """

    json_dish = json.dumps(dish, cls=DishJsonEncoder)

    assert json.loads(expected_json) == json.loads(json_dish)
    