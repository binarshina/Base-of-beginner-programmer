"""Пример множественного наследования."""


class Engine:
    def start(self):
        print("Двигатель заведен")


class Wheels:
    def start(self):
        print("Колеса начали крутиться")


class Car(Engine, Wheels):
    pass


my_car = Car()
my_car.start()  # Выведет: "Двигатель заведен"
# (сначала вызывается метод из Engine, так как он указан первым)
