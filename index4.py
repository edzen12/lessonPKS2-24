class Computer:
    def __init__(self, comp_id, hourly_rate):
        self.__id = comp_id
        self.__hourly_rate = hourly_rate  # цена за час
        self._is_busy = False
        self._current_client = None
        self._hours = 0

    @property
    def id(self):
        return self.__id

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, new_rate):
        if 50 <= new_rate <= 1000:
            self.__hourly_rate = new_rate
            print(f"Тариф для компьютера {self.__id} изменён на {new_rate} сом/ч.")
        else:
            print("Недопустимое значение тарифа (должно быть от 50 до 1000 сом).")

    def start_session(self, client, hours):
        """Запуск игровой сессии"""
        if self._is_busy:
            print(f"Компьютер {self.id} уже занят.")
            return False

        cost = self.__hourly_rate * hours
        if client.pay(cost):
            self._is_busy = True
            self._current_client = client
            self._hours = hours
            print(f"{client.name} начал сессию на компьютере {self.id} ({hours} ч, {cost} сом).")
            return True
        else:
            print(f"У клиента {client.name} недостаточно средств.")

class Client:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance  # защищённый атрибут

    @property
    def balance(self): 
        return self._balance

    @balance.setter
    def balance(self, new_balance): 
        if new_balance < 0:
            print("Баланс не может быть отрицательным.")
        else:
            self._balance = new_balance

    def add_balance(self, amount): 
        if amount > 0:
            self._balance += amount
            print(f"Баланс пополнен на {amount} сом. Текущий баланс: {self._balance} сом.")
            return True
        else:
            print("Введите корректную сумму для пополнения.")
            return False

    def pay(self, amount): 
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            print(f"Недостаточно средств. Баланс: {self._balance} сом, нужно: {amount} сом.")
            return False

    def info(self): 
        return f"Клиент: {self.name}, Баланс: {self._balance} сом"

class Club:
    def __init__(self, name):
        self.name = name
        self.computers = []  # список объектов Computer
        self._income = 0  # защищённый атрибут, выручка клуба

    def add_computer(self, computer):
        self.computers.append(computer)
        print(f"Компьютер добавлен: {computer.id}, тариф {computer.hourly_rate} сом/ч")

    def find_free_computer(self): 
        for comp in self.computers:
            if not comp._is_busy:
                return comp
        return None

    def serve_client(self, client, hours): 
        free_comp = self.find_free_computer()
        if not free_comp:
            print("Нет свободных компьютеров")
            return

        if free_comp.start_session(client, hours): 
            self._income += free_comp.hourly_rate * hours

    def end_all_sessions(self):  
        for comp in self.computers:
            comp.end_session()
        print("Все игровые сессии завершены")

    def show_status(self): 
        print(f" Клуб '{self.name}':")


b = Club("HunerHunerClub")
b.add_computer(Computer(1,100))
b.add_computer(Computer(2,150))
b.add_computer(Computer(3,180))
x = Client('Malika', 500)
y = Client('Aliya', 100)
b.serve_client(y, 2)
b.serve_client(x, 3.5)
b.show_status()


