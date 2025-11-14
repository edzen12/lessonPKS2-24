class BaseBook:
    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        self.__price  = price
        
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if value >= 100:
            self.__price = value

    def info(self):
        return f"{self._title}, автор: {self._author} Стоимость: {self.price}сом"

class Book(BaseBook):
    def info(self):
        return f"Книга: {self._title}, автор: {self._author} Стоимость: {self.price}сом"
    
class EBook(BaseBook):
    def __init__(self, title, author, price, file_size_mb):
        super().__init__(title, author, price)
        self._file_size_mb = file_size_mb
    
    def info(self):
        return f"Электронная книга: {self._title}, автор: {self._author}, цена: {self.price}сом, файл: {self._file_size_mb}МБ"
    
class AudioBook(BaseBook):
    def __init__(self, title, author, price, duration_min):
        super().__init__(title, author, price)
        self._duration_min = duration_min
    
    def info(self):
        return f"Аудиокнига: {self._title}, автор: {self._author}, цена: {self.price}сом, длительность: {self._duration_min}мин"
    
class Inventory:
    def __init__(self):
        self._books = []
  
    def add_books(self, *books): #принимает любое количество объектов книг
        for book in books:
            if not isinstance(book, BaseBook):
                raise TypeError("Можно добавлять только объекты книг")
            self._books.append(book)

    def find_books(self, **filters):
        result = self._books
        for key, value in filters.items():
            attr_name = f"_{key}" 
            result = [b for b in result if getattr(b, attr_name, None) == value]
        return result


    def remove_book(self, book): #удаляет книгу
        if book in self._books:
            self._books.remove(book)

    def all_books(self): #возвращает копию списка книг
        return self._books.copy()

class BookStore:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self.__income = 0
    
    @property
    def income(self):
        return self.__income
    
    def sell_book(self, title): #ищет по названию, удаляет книгу, увеличивает доход
            for book in self.inventory.all_books():
                if book._title == title:
                    self.__income += book.price
                    self.inventory.remove_book(book)
                    return True
            return False

    def show_status(self):
        return {
            'магазин': self.name,
            'доход': self.__income,
            'книги': [b.info() for b in self.inventory.all_books()],
        }

b1 = Book('Война и мир', "Толстой", 600)
b2 = EBook('Грокаем алгоритмы', "Гена алк", 800, file_size_mb=10)
b3 = AudioBook('Python основы жизни', "Мудрецов", 500, duration_min=700)

store = BookStore('Книжный дом')
store.inventory.add_books(b1,b2,b3)

found = store.inventory.find_books(author='Мудрецов')
for book in found:
    print(book.info())

store.sell_book('Грокаем алгоритмы')
print(store.show_status())
 