# ооп - объектно-ориентированное программирование
    # Наследование
    # Инкапсуляция
    #     public 
    #     _protected
    #     __private
    # Полиморфизм

# class - создания класса, имя класса всегда пишется с большой
# def __init__() - конструктор класса, 
# self - cсылка на метод и атрибуты внутри класса
# self.name - атрибутом класса
# n = Cat() - экземпляром класса
# @property - он метод делает так чтобы он работал как атрибут, но внутри все такой же метод
#     getter - получает
#     setter - изменяет
#     deleter - удаляет

class Animal:
    def __init__(self, name, age):
        self.__net = name
        self.age = age
    
    @property
    def name(self): # метод класса
        return self.__net
    @name.setter
    def name(self, val):
        self.__net = val

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
