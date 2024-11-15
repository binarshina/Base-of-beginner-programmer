"""Пример использования конструктора и деструктора."""


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __del__(self):
        print(f"Объект {self.brand} {self.model} удален")
