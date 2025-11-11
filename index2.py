class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")

class Employee(Person):
    def __init__(self, name, age, salary, position):
        super().__init__(name, age)
        self.salary = salary
        self.position = position 
    
    def calculate_salary(self): #возвращает месячную зарплату
        return self.salary

    def info(self):
        person =  super().info()
        print(f"{person} Должность: {self.position}, Зарплата: {self.salary}")

# 3. Подклассы сотрудников:
# Chef — повар.
# Метод: cook(dish_name) → печатает "Повар {name} готовит {dish_name}".
# Waiter — официант.
# Метод: take_order(dish_list) → создаёт и возвращает объект класса Order.
# Manager — менеджер.
# Метод: calculate_profit(income, expenses) → возвращает прибыль (income - expenses).
# 4. Класс Dish
# Атрибуты: name, price, ingredients (список строк)
# Метод: __str__() — возвращает "Блюдо: {name}, Цена: {price}, Ингредиенты: {', '.join(ingredients)}"
# 5. Класс Menu
# Атрибут:dishes (список объектов Dish)
# Методы: add_dish(dish), remove_dish(name), 
# find_dish(name) — возвращает блюдо по имени.
# show_menu() — выводит всё меню красиво.

# 6. Класс Order
# Атрибуты: dishes, total, is_paid
# Методы:add_dish(dish), calculate_total() — суммирует цены блюд.
# pay() — устанавливает is_paid = True и печатает чек.

# 7. Класс Restaurant
# Атрибуты: name, menu, employees, orders
# Методы: add_employee(employee), add_order(order), show_employees()
# show_orders(), total_income() — возвращает общую сумму оплаченных заказов.