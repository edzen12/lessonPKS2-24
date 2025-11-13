class Tour:
    def __init__(self, id, price, days):
        self.__id = id
        self.__price = None #приватный атрибут price
        self.price = price #установленный setter
        self._is_booked = False
        self._client = None
        self._days = days
    
    @property
    def id(self):
        return self.__id

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value >= 5000:
            self.__price = value
        else:
            print('цена не может быть ниже 5000 сом')

    def book(self, client): # бронирует тур, делает его недоступным, если клиент оплатил.
        if self._is_booked:
            return False
        self._is_booked = True # делает его недоступным True-недоступно, False-доступно
        self._client = client
        return True

    def cancel_booking(self): #отменяет бронь, делает тур доступным.
        if not self._is_booked:
            return False
        self._is_booked = False #делает тур доступным
        self._client = None
        return True

    def info(self):
        return {
            'id': self.__id,
            'price': self.__price,
            'days': self._days,
            'is_booked': self._is_booked,
            'client': self._client, 
        }

class Client:
    def __init__(self, name:str, balance:float):
        self.name = name
        self.balance = balance 

    def pay(self, amount): #уменьшает баланс, если хватает денег;
        if amount <= 0 :
            return False
        if self.balance < amount:
            return False
        self.balance -= amount
        return True
    
    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            return False
        
    def info(self):
        return f"Имя: {self.name} Баланс: {self.balance}сом"

# 3. Класс Agency
# Атрибуты:
# name — название агентства;
# tours — список объектов Tour;
# _income — защищённый атрибут (доход агентства).

# Методы:
# add_tour(tour) — добавляет новый тур;
# show_available_tours() — показывает все свободные туры;
# book_tour(client, tour_id) — бронирует тур для клиента;
# cancel_all_bookings() — отменяет все активные брони;
# show_status() — показывает состояние всех туров и текущую выручку.

