"""Базовый пример наследования классов."""


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  # Марка автомобиля
        self.model = model  # Модель автомобиля
        self.year = year  # Год выпуска

    def drive(self):
        print(f"{self.brand} {self.model} едет!")


# Дочерний класс ElectricCar, наследующийся от Car
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_level=100):
        # Вызов конструктора родительского класса
        super().__init__(brand, model, year)
        self.battery_level = battery_level

    def charge(self):
        """Метод для подзарядки батареи."""
        self.battery_level = 100
        print(f"Батарея полностью заряжена для {self.brand} {self.model}.")


# Пример использования классов

my_electric_car = ElectricCar("Tesla", "Model S", 2022)
my_electric_car.drive()  # Использует метод из родительского класса
print(f"Уровень заряда батареи: {my_electric_car.battery_level}%")
my_electric_car.charge()  # Использует метод класса ElectricCar
