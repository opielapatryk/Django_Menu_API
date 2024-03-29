from repository.memrepo import MemRepo
from use_cases.dish_list import dish_list_use_case
from django.http import HttpResponse
import json
from serializers.dish import DishJsonEncoder

dishes = [
    {
    "id" : 1,
    "name": "pizza",
    "description": "italy",
    "price": 10.99
    },
    {
    "id" : 2,
    "name": "burger",
    "description": "american",
    "price": 7.99
    },
    {
    "id" : 3,
    "name": "spaghetti",
    "description": "italy",
    "price": 5.99
    },
    {
    "id" : 4,
    "name": "fries",
    "description": "american",
    "price": 1.99
    },
]

def dish_list(request):
    repo = MemRepo(dishes) 
    result = dish_list_use_case(repo)
    
    serialized_result = json.dumps(result, cls=DishJsonEncoder)
    return HttpResponse(serialized_result)

