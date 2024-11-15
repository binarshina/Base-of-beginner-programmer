from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print(f"Отправка Email: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"Отправка SMS: {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"Отправка Push: {message}")
