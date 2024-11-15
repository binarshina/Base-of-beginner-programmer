from abc import ABC, abstractmethod


class Writeable(ABC):
    @abstractmethod
    def write_data(self, data):
        pass


class Notifiable(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass


class Printable(ABC):
    @abstractmethod
    def print_document(self, document):
        pass


class NotificationTask(Notifiable):
    def send_notification(self, message):
        print(f"Отправка уведомления: {message}")


class PrintTask(Printable):
    def print_document(self, document):

        print(f"Печать документа: {document}")
