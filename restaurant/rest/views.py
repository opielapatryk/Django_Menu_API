from repository.memrepo import MemRepo
from repository.mongorepo import MongoRepo
from use_cases.dish_list import dish_list_use_case
from use_cases.dish_get import dish_get_use_case
from use_cases.dish_post import dish_post_use_case
from use_cases.dish_put import dish_put_use_case
from use_cases.dish_delete import dish_delete_use_case
from django.http import HttpResponse, HttpResponseBadRequest
import json
from serializers.dish import DishJsonEncoder

mongo_configuration = {
    "MONGODB_HOSTNAME": 'db',
    "MONGODB_PORT": 27017,
    "MONGODB_USER": 'root',
    "MONGODB_PASSWORD": 'mongodb',
    "APPLICATION_DB": 'restaurant',
}

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
    if request.method == 'GET':
        repo = MongoRepo(mongo_configuration)
        result = dish_list_use_case(repo)
        
        serialized_result = json.dumps(result, cls=DishJsonEncoder)
        return HttpResponse(serialized_result)

def dish_get(request, pk):
    if request.method == 'GET':
        dish_id = pk
        repo = MongoRepo(mongo_configuration)
        dish = dish_get_use_case(repo, dish_id)
        
        if dish:
            serialized_dish = json.dumps(dish, cls=DishJsonEncoder)
            return HttpResponse(serialized_dish, content_type='application/json')
        else:
            return HttpResponse(status=404)
    
def dish_post(request):
    if request.method == 'POST':
        dish = json.loads(request.body)

        id = dish.get('id')
        name = dish.get('name')
        description = dish.get('description')
        price = dish.get('price')

        if not name or not description or not price or not id:
            return HttpResponseBadRequest("Missing required fields")
        
        new_dish_data = {
            "id": id,
            "name": name,
            "description": description,
            "price": price
        }

        repo = MongoRepo(mongo_configuration)
        created_dish = dish_post_use_case(repo, new_dish_data)
        
        if created_dish:
            serialized_dish = json.dumps(created_dish, cls=DishJsonEncoder)
            return HttpResponse(serialized_dish, content_type='application/json', status=201)

def dish_put(request):
    if request.method == 'PUT':
        dish = json.loads(request.body)

        id = dish.get('id')
        name = dish.get('name')
        description = dish.get('description')
        price = dish.get('price')

        if not name or not description or not price or not id:
            return HttpResponseBadRequest("Missing required fields")
        
        updated_dish_data = {
            "id": id,
            "name": name,
            "description": description,
            "price": price
        }

        repo = MongoRepo(mongo_configuration)
        updated_dishes = dish_put_use_case(repo, updated_dish_data)
        
        if updated_dishes:
            serialized_dishes = json.dumps(updated_dishes, cls=DishJsonEncoder)
            return HttpResponse(serialized_dishes, content_type='application/json')

def dish_delete(request, pk):
    if request.method == 'DELETE':
        repo = MongoRepo(mongo_configuration)
        dishes_after_delete = dish_delete_use_case(repo, pk)
        
        if dishes_after_delete:
            serialized_dishes = json.dumps(dishes_after_delete, cls=DishJsonEncoder)
            return HttpResponse(serialized_dishes, content_type='application/json')
