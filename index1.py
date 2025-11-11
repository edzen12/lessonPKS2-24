class Transport:
    def __init__(self, speed, capacity):
        self._speed = speed  # текущая скорость (км/ч)
        self._capacity = capacity  # вместимость (кол-во)

    def start(self):  # сообщение, что транспорт начал движение
        print("Транспорт начал движение")

    def stop(self):  # сообщение, что транспорт остановился
        print("Транспорт остановил движение")

    def info(self):  # возвращает строку с основной инфо о транспорте
        return f"Скорость: {self._speed} км/ч, вместимость: {self._capacity} чел"


class Car(Transport):
    def __init__(self, speed, capacity, brand):
        super().__init__(speed, capacity)
        self.brand = brand  # марка автомобиля

    def info(self):
        base_info = super().info()
        return f"Автомобиль {self.brand}. {base_info}"


class Bus(Transport):
    def __init__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.route_number = route_number  # номер маршрута

    def info(self):
        base_info = super().info()
        return f"Автобус маршрута №{self.route_number}. {base_info}"


class Electric:
    def __init__(self, battery_level):
        self._battery_level = battery_level  # уровень заряда батареи (%)

    def charge(self):  # заряжает батарею до 100%
        self._battery_level = 100
        print("Батарея заряжена")

    def battery_status(self):  # показывает уровень заряда
        print(f"Заряд батареи: {self._battery_level}%")


class ElectricCar(Car, Electric):
    def __init__(self, speed, capacity, brand, battery_level):
        Car.__init__(self, speed, capacity, brand)
        Electric.__init__(self, battery_level)

    def info(self):
        car_info = Car.info(self)
        return f"Электромобиль {self.brand}. {car_info}. Заряд: {self._battery_level}%"


tesla = ElectricCar(120, 5, 'Tesla', 85)
tesla.start()
tesla.charge()
print(tesla.info())

bus = Bus(50, 40, 13)
bus.start()
print(bus.info())