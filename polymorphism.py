"""Пример полиморфизма"""


class Car:
    def drive(self):
        print("Машина едет по дороге.")


class Boat:
    def drive(self):
        print("Лодка плывет по воде.")


class Airplane:
    def drive(self):
        print("Самолет летит в небе.")


vehicles = [Car(), Boat(), Airplane()]

for vehicle in vehicles:
    vehicle.drive()
