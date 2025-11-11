# Декораторы  добавляют функциональность в существующий код
# Декоратор - это паттерн программирования, который позволяет добавлять новый функционал к нашей сущ.функции

# функция - это объект
def great():
    print("Привет")

hello = great
hello()
# №№№№№№№
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func):
    message = func('Hello PKS-2-24')
    print(message)

speak(shout)
speak(whisper)

###

def inc(x):
    return x+1

def dec (x):
    return x-1

def operate(func, x):
    result = func(x)
    return result

print(operate(inc, 6))
print(operate(dec, 8))

######
def oute():
    def inner():
        print('Я функция внутри')
    return inner 
# oute - возвращает другую функцию
newFunc = oute()
newFunc()
######
def before_after(func):
    def wrapper():
        print("Перед вызовом")
        func()
        print("После вызова")
    return wrapper

@before_after # декоратор
def say_Hi():
    print("Привет друг")

say_Hi()

# №№№№№№№№
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} c аргументами {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@logger
def add(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

add(5,10,5)
add(a=5, b=8)

#######

# @property - это встроенный декоратор
    # getter - получает
    # setter - изменяет
    # deleter - удаляет
# позволяет нам обращаться к методу как к обычному полю атрибута

# без @property
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    def get_area(self):
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.get_area())

##### c декоратором @property
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

    @name.setter  
    def name(self, value):
        print("сеттер сработал")
        if not isinstance(value, str): # проверяет не явл ли value стр
            raise ValueError("Имя должно быть строкой")
        self._name = value  
    
    @name.deleter
    def name(self):
        print("Имя удалено")
        del self._name

p = Person('Gena')
p.name = 'Alez'
print(p.name)
del p.name 

# след урок: другие магические метода, другие декораторы