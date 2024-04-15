from repository.memrepo import MemRepo
from repository.mongorepo import MongoRepo
from repository.postgrerepo import PostgresRepo
from use_cases.dish_list import dish_list_use_case
from use_cases.dish_get import dish_get_use_case
from use_cases.dish_post import dish_post_use_case
from use_cases.dish_put import dish_put_use_case
from use_cases.dish_patch import dish_patch_use_case
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

postgres_configuration = {
    "POSTGRES_USER": 'postgres',
    "POSTGRES_PASSWORD": 'postgres',
    "POSTGRES_HOSTNAME": 'db',
    "POSTGRES_PORT": 5432,
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

def dish_view(request):
    if request.method == 'GET':
        repo = PostgresRepo(postgres_configuration)
        result = dish_list_use_case(repo)
        
        
        serialized_result = json.dumps(result, cls=DishJsonEncoder)
        return HttpResponse(serialized_result)
    
    if request.method == 'POST':
        dish = json.loads(request.body)

        id = dish.get('id')
        name = dish.get('name')
        description = dish.get('description')
        price = dish.get('price')

        if not name or not description or not price or not id:
            return HttpResponseBadRequest(json.dumps({"message":"Missing required fields"}))
        
        new_dish_data = {
            "id": id,
            "name": name,
            "description": description,
            "price": price
        }

        repo = PostgresRepo(postgres_configuration)
        
        try:
            created_dish = dish_post_use_case(repo, new_dish_data)
        except Exception as e:
            error_message = str(e)
            if 'duplicate key value violates unique constraint "dishes_pkey"' in error_message:
                return HttpResponse(json.dumps({"message": "Dish with this ID already exists"}), content_type='application/json', status=409)
            else:
                return HttpResponseBadRequest(json.dumps({"message": "Integrity error occurred"}))

        if created_dish:
            serialized_dish = json.dumps(created_dish, cls=DishJsonEncoder)
            return HttpResponse(serialized_dish, content_type='application/json', status=201)
        else:
            return HttpResponse(json.dumps({"message": "Dish already exists"}),content_type='application/json',status=404)

    if request.method == 'PUT':
        dish = json.loads(request.body)

        id = dish.get('id')
        name = dish.get('name')
        description = dish.get('description')
        price = dish.get('price')

        if not name or not description or not price or not id:
            return HttpResponseBadRequest(json.dumps({"message":"Missing required fields"}))
        
        updated_dish_data = {
            "id": id,
            "name": name,
            "description": description,
            "price": price
        }

        repo = PostgresRepo(postgres_configuration)
        updated_dishes = dish_put_use_case(repo, updated_dish_data)
        print(updated_dishes)
        
        if updated_dishes:
            serialized_dishes = json.dumps(updated_dishes, cls=DishJsonEncoder)
            return HttpResponse(serialized_dishes, content_type='application/json')
        else:
            return HttpResponse(json.dumps({"message": "Dish not found"}),content_type='application/json',status=404)

def dish_pk_view(request, pk):
    if request.method == 'GET':
        dish_id = pk
        repo = PostgresRepo(postgres_configuration)
        dish = dish_get_use_case(repo, dish_id)
        
        if dish:
            serialized_dish = json.dumps(dish, cls=DishJsonEncoder)
            return HttpResponse(serialized_dish, content_type='application/json')
        else:
            return HttpResponse(json.dumps({"message": "Dish not found"}),content_type='application/json',status=404)
        
    if request.method == 'PATCH':
        dish = json.loads(request.body)
        dish_id = pk

        updated_dish_data = {}

        if dish.get('name') is not None: updated_dish_data['name'] = dish.get('name')
        if dish.get('description') is not None: updated_dish_data['description'] = dish.get('description')
        if dish.get('price') is not None: updated_dish_data['price'] = dish.get('price')

        repo = PostgresRepo(postgres_configuration)
        updated_dishes = dish_patch_use_case(repo, updated_dish_data, dish_id)
        
        if updated_dishes:
            serialized_dishes = json.dumps(updated_dishes, cls=DishJsonEncoder)
            return HttpResponse(serialized_dishes, content_type='application/json')
        else:
            return HttpResponse(json.dumps({"message": "Dish not found"}),content_type='application/json',status=404)

    if request.method == 'DELETE':
        repo = PostgresRepo(postgres_configuration)
        dishes_after_delete = dish_delete_use_case(repo, pk)
        
        if dishes_after_delete:
            serialized_dishes = json.dumps(dishes_after_delete, cls=DishJsonEncoder)
            return HttpResponse(serialized_dishes, content_type='application/json')
        else:
            return HttpResponse(json.dumps({"message": "Dish not found"}),content_type='application/json',status=404)