class Ingredient:
    def __init__(self, name, quantity, price_per_gram):
        self._name = name
        self._quantity = quantity #в граммах
        self.__price_per_gram = None
        self.price_per_gram = price_per_gram #то что через setter
        
    @property
    def price_per_gram(self):
        return self.__price_per_gram
    @price_per_gram.setter
    def price_per_gram(self, value):
        if value>0.1:
            self.__price_per_gram = float(value)
        else:
            raise ValueError("цена не может быть ниже 0.1")

    def cost(self, weight_grams): #возвращает стоимость weight граммов
        return float(weight_grams) * self.__price_per_gram
    
    def use(self, weight_grams):
        if weight_grams <= 0 or weight_grams > self._quantity:
            return False
        self._quantity -= weight_grams
        return True
    
    def info(self):
        return f"{self._name}: запас {self._quantity:2f}г, {self.__price_per_gram}сом/г"

class Dish:
    def __init__(self, name, ingredients, base_price):
        self._name = name
        self._ingredients = dict(ingredients) #словарь: ингредиент → граммы
        self.__base_price = None
        self.base_price = base_price
    
    @property
    def base_price(self):
        return self.__base_price
    @base_price.setter
    def base_price(self, value):
        if value >= 20:
            self.__base_price = value
    
    def total_cost(self): #стоимость ингредиентов + base_price
        total = 0.0
        for ing, grams in self._ingredients.items():
            total += ing.cost(grams)
        total+=self.__base_price
        return round(total, 2)
    
    def info(self):
        return f"{self._name}, цена {self.total_cost():.2f}сом" 

# Наследники Dish:
class HotDish(Dish): #горячее блюдо
    def __init__(self, name, ingredients, base_price, spicy_level):
        super().__init__(name, ingredients, base_price)
        self._spicy_level = spicy_level #0–5

    def info(self):
        return f"Горячее блюдо: {self._name}, острота {self._spicy_level}, цена {self.total_cost():.2f} сом" 

class Dessert(Dish):
    def __init__(self, name, ingredients, base_price, sweetness):
        super().__init__(name, ingredients, base_price)
        self._sweetness=sweetness #0–10
    
    def info(self):
        return f"«Десерт: {self._name}, сладость {self._sweetness}, цена {self.total_cost():.2f} сом"  

class Drink(Dish):
    def __init__(self, name, ingredients, base_price, volume_ml):
        super().__init__(name, ingredients, base_price)
        self._volume_ml=volume_ml
    
    def info(self):
        return f"«Напиток: {self._name}, объем {self._volume_ml}мл, цена {self.total_cost():.2f} сом"    

class Kitchen:
    def __init__(self):
        self._dishes = []
        
    def add_dishes(self, *dishes): #принимает любое количество блюд
        for d in dishes:
            self._dishes.append(d)

    def find_dishes(self, **filters): #поиск по любым параметрам
        res = self._dishes
        for key, value in filters.items():
            if key == 'price':
                res = [d for d in res if d.total_cost() == value]
            else:
                attr_name = f"_{key}"
                res = [d for d in res if getattr(d, attr_name, None)==value]
        return res 

    def remove_dish(self, dish):
        if dish in self._dishes:
            self._dishes.remove(dish)

    def all_dishes(self): 
        return self._dishes.copy()

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.kitchen = Kitchen()
        self.__income = 0.0
    
    @property
    def income(self):
        return self.__income
    
    def order_dish(self, dish_name): #продаёт блюдо, увеличивает доход, убирает из меню
        for dish in self.kitchen.all_dishes():
            if getattr(dish, "_name", None) == dish_name:
                self.__income += dish.total_cost()
                self.kitchen.remove_dish(dish)
                return True
        return False
    
    def menu(self): #список всех блюд через info()
        return [d.info() for d in self.kitchen.all_dishes()]
    
    def status(self): #доход и количество оставшихся блюд
        return {
            'Ресторан': self.name,
            'Доход': self.income,
            'Блюда': len(self.kitchen.all_dishes())
        }
meat = Ingredient("Мясо", 5000, 0.8)      # 0.8 сом/г
cabbage = Ingredient("Капуста", 3000, 0.2)
potato = Ingredient("Картофель", 2000, 0.15)
sugar = Ingredient("Сахар", 1000, 0.5)
milk = Ingredient("Молоко", 2000, 0.25)
water = Ingredient("Вода", 10000, 0.01)
borsh_ingredients = {meat: 150, cabbage: 100, potato: 120, water: 200}
borsh = HotDish("Борщ", borsh_ingredients, base_price=50, spicy_level=1)
cake_ingredients = {sugar: 200, milk: 300}
cake = Dessert("Торт", cake_ingredients, base_price=40, sweetness=9)
lemonade_ingredients = {sugar: 50, water: 300}
lemonade = Drink("Лимонад", lemonade_ingredients, base_price=20, volume_ml=300)
rest = Restaurant("Домашний Ресторан")
rest.kitchen.add_dishes(borsh, cake, lemonade)

print("Меню:")
for line in rest.menu():
    print(" -", line)
 
spicy_dishes = rest.kitchen.find_dishes(spicy_level=1)
print("\nГорячие блюда с остротой 1:")
for d in spicy_dishes:
    print(" ->", d.info())
 
print("\nЗаказываем 'Борщ':", rest.order_dish("Борщ"))
print("Заказываем 'Борщ' ещё раз (должно вернуть False):", rest.order_dish("Борщ"))
 
print("\nСтатус ресторана:", rest.status())
 
print("\nОставшееся меню:")
for line in rest.menu():
    print(" -", line)