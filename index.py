# Типы данных
#     int, float, bool,str 
#     list []
#     dict {}
#     tuple ()
#     set {} frozenset 
#     None 

# Ввод и вывод (input, print)

# Переменные - хранить любой тип данных и работать с ней
# name = "var"

# Операторы сравнения > < >= <= != == 
# Ариф операторы + - * / ** // % += -= /= *= 

# Условные операторы if elif else 

# циклы - повторение одного и того же действия
# for - для, while - пока 

# исключения try except

# индексы 01234
# срезы [start:stop:step]

# методы: 
#     str-строк - .lower() .upper() 
#     dict-словарей .keys() values() .items()
#     list-списков .append() .remove() .pop() .reverse()
#     set-множества .remove() .add() .pop() 

# Тернарный оператор
# list comprehension - генератор списков
# chislo = [i for i in range(100) if i % 2 ==0]
# print(chislo)

# Работа с файлами r w a x b rb wb

# функции 
#     встроенные 
#         print() input() type() len() map() filter()
#     пользовательские
#         lambda - анонимные функции, функции без имени
#         def - именем и возможно с параметрами или без

# Закочилась База, началось программирвоание
# OOP - ООП - объектно-ориентированное программирование
class Student:
    def __init__(self, fullname, age, group): # конструктор 
        self.fullname = fullname # атрибут класса
        self.__age = age # атрибут класса
        self._group = group # атрибут класса
    
    def info(self): # метод класса
        return f"{self.fullname} {self.__age} {self._group}"

st = Student('Denis Denisov', 17, 'pks-2-24') # экземпляр
print(st.info())

def calc():
    print('hello')

calc()