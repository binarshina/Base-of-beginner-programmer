class Engine:
    def start(self):
        print("Двигатель заведен")


class Car:
    def __init__(self, engine=None):
        self.engine = engine  # Объект Engine передается в Car, но не создается внутри

    def set_engine(self, engine):
        # Позволяет назначить двигатель, если его не было при создании
        self.engine = engine

    def start(self):
        if self.engine:
            self.engine.start()
        else:
            print("Двигатель не установлен.")
