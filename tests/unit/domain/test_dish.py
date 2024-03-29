from restaurant.domain.dish import Dish

def test_dish_model_init():
    dish = Dish(
        'pierogi','polish dish',9.99
    )

    assert dish.name == 'pierogi'
    assert dish.description == 'polish dish'
    assert dish.price == 9.99
