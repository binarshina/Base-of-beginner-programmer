class Engine:
    def start(self):
        print("Двигатель заведен")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


# Создание экземпляра Engine
engine = Engine()

# Создание экземпляра Car с использованием объекта Engine
my_car = Car(engine)

# Запуск автомобиля, который в свою очередь запускает двигатель
print(my_car.start())
