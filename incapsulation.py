"""Примерный класс Building с приватными атрибутами и публичными методами управления"""


class Building:
    def __init__(
        self,
        heating_system_status="выкл",
        electricity_status="выкл",
        water_supply_status="выкл",
    ):
        # Закрытые (приватные) атрибуты системы здания
        self.__heating_system_status = (
            heating_system_status  # Отопительная система (включена/выключена)
        )
        self.__electricity_status = (
            electricity_status  # Электрическая система (включена/выключена)
        )
        self.__water_supply_status = (
            water_supply_status  # Система водоснабжения (включена/выключена)
        )

    def set_heating_system(self, status):
        """Публичный метод для управление отоплением."""
        if status in ["вкл", "выкл"]:
            self.__heating_system_status = status
            print(f"Система отопления сейчас {status}.")
        else:
            print("Неправильный статус системы отопления. Используй 'вкл' or 'выкл'.")

    def set_electricity(self, status):
        """Публичный метод для управления электричеством"""
        if status in ["вкл", "выкл"]:
            self.__electricity_status = status
            print(f"Электричество сейчас {status}.")
        else:
            print(
                "Неправильный статус системы подачи электричества. Используй 'вкл' or 'выкл'."
            )

    def set_water_supply(self, status):
        """Публичный метод для управления водоснабжением."""
        if status in ["вкл", "выкл"]:
            self.__water_supply_status = status
            print(f"Водоснабжение сейчас {status}.")
        else:
            print(
                "Неправильный статус системы водоснабжения. Используй 'вкл' or 'выкл'."
            )

    def display_status(self):
        """Публичеый метод для мониторинга всех систем в здании."""
        print("Статус систем в здании:")
        print(f"Система отопления: {self.__heating_system_status}")
        print(f"Электричество: {self.__electricity_status}")
        print(f"Водоснабжение: {self.__water_supply_status}")


# Пример использования класса Building
my_building = Building()
my_building.display_status()  # Показать текущий статус систем

# Управление системами только через публичные методы
my_building.set_heating_system("вкл")  # Включаем отопление
my_building.set_electricity("вкл")  # Включаем электричество
my_building.set_water_supply("вкл")  # Включаем водоснабжение
my_building.display_status()  # Показать обновленный статус систем

# Прямой доступ к приватным атрибутам невозможен, попытка вызовет ошибку:
# my_building.__heating_system_status = "выкл"  # Ошибка! Это защищенный атрибут.
