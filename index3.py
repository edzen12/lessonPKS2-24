class Person:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def deposit(self, amount): # пополнение счёта.
        self.balance+=amount
        return self.balance
    
    def withdraw(self, amount): # снятие счёта
        if amount<self.balance:
            self.balance-=amount
            print(f"Вы сняли {amount}сом, осталось: {self.balance}сом")
        else:
            print(f"Недостаточно денег, у вас {self.balance}сом")

    def info(self):
        print(f"{self.name} Возраст:{self.age} Денег:{self.balance}сом")

class Bank:
    def __init__(self, name):
        self.name = name 
        self.clients = [] # список объектов Person
        self.products = [] # (депозиты, кредиты, рассрочки)
        self.income = 0 # доход банка

    def add_client(self, client):
        self.clients.append(client)
        print(f"Клиент {client.name} добавлен")

    def add_product(self, product):
        self.products.append(product)
        print(f"Продукт  добавлен")

    def add_income(self, amount):
        self.income += amount

    def calculate_total_profit(self):
        return self.income
     
    def show_clients(self):
        print("НАши клиенты: ")
        for i in self.clients:
            print(f".  {i.info()}") 

    def show_products(self):
        print("НАши Продукты: ")
        for i in self.products:
            print(f".  {i.info()}")

class BankProduct:
    def __init__(self, client, amount, interest_rate, term_months):
        self.client = client # клиент
        self.amount = amount # сумма
        self.interest_rate = interest_rate #процентная ставка
        self.term_months = term_months #срок в месяцах
    
    def calculate_interest(self): #рассчитывает сумму процентов
        return self.amount * (self.interest_rate / 100) * (self.term_months / 12)

    def info(self):
        print(f"{self.client.name} сумма: {self.amount}сом, ставка: {self.interest_rate}%, срок: {self.term_months} мес")

class Deposit(BankProduct):
    # Деньги клиента передаются банку, и по окончании срока клиент получает сумму + проценты.
    def close_deposit(self, bank):
        if self.client.withdraw(self.amount):
            profit = self.calculate_interest()
            payout = self.amount + profit
            self.client.deposit(payout)
            bank.add_income(profit * 0.01) #банк забирает себе 10% от процентов
            print(f"Депозит закрыт: клиент {self.client.name} получил {payout}сом (включая {profit}сом в процентах)")
        else:
            print("Недостаточно денег чтобы открыть депозит") 

class Credit(BankProduct):
    # Банк выдаёт клиенту деньги, которые тот должен вернуть с процентами.
    def monthly_payment(self): # рассчитывает ежемесячный платёж по кредиту.
        total = self.amount+self.calculate_interest()
        return round(total / self.term_months, 2)

    def close_credit(self, bank): #возвращает банку кредита и проценты(уменьшает баланс клиента)
        self.client.deposit(self.amount)
        total_payment = self.amount + self.calculate_interest()
        if self.client.withdraw(total_payment):
            bank.add_income(self.calculate_interest())
            print(f"Кредит закрыт {self.client.name} выплатил {total_payment}сом (включая проценты)")
        else:
            print(f'{self.client.name} не смог погасить кредит')

# 6. класс Installment (Рассрочка)
# Клиент покупает товар в рассрочку (без процентов, но с комиссией).
# Атрибуты: product_name, commission_rate
# Методы: monthly_payment(), close_installment()

bank = Bank('PKS Bank')
zahid = Person('Zahid', 17, 100)
aibiike = Person('Aibiike', 18, 300)
bank.add_client(zahid)
bank.add_client(aibiike)
bank.show_clients()
deposit = Deposit(zahid, amount=4050, interest_rate=8, term_months=12)
bank.add_product(deposit)
