from domain.dish import Dish


class MemRepo:
   def __init__(self, data):
      self.data = data
   
   def list(self):
      return [Dish.from_dict(d) for d in self.data]
    
   def get(self, id):
      try:
         dish = [Dish.from_dict(dish) for dish in self.data if dish['id'] == id]
         return dish
      except (IndexError, ValueError):
         return None

   def post(self, dish):
      self.data.append(dish)
      result = [Dish.from_dict(i) for i in self.data]

      return result

   def put(self, updated_dish):
      updated_data = []

      for dish in self.data:
         if dish['id'] == updated_dish['id']:
               updated_data.append(updated_dish)
         else:
               updated_data.append(dish)

      result = [Dish.from_dict(dish) for dish in updated_data]
      
      return result
   
   def delete(self, id):
      for dish in self.data:
         if dish['id'] == id:
               self.data.remove(dish)

      result = [Dish.from_dict(dish) for dish in self.data]
      
      return result
