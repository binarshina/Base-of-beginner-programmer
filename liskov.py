class Bird:
    def make_sound(self):
        print("Птица издает звук")


# Летающие птицы наследуют этот класс
class FlyingBird(Bird):
    def fly(self):
        print("Птица летит")


# Нелетающие птицы наследуют этот класс
class NonFlyingBird(Bird):
    def walk(self):
        print("Птица идет")


# Конкретные реализации
class Sparrow(FlyingBird):
    pass


class Penguin(NonFlyingBird):
    pass
