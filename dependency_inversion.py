from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Отправка Email: {message}")


class SMSNotifier(Notifier):
    def send(self, message):
        print(f"Отправка SMS: {message}")


class OrderService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def process_order(self, order):
        print(f"Заказ {order} обработан")
        self.notifier.send(f"Уведомление: заказ {order} был успешно обработан")


email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

order_service = OrderService(email_notifier)
order_service.process_order(
    "12345"
)  # Выведет: Отправка Email: Уведомление: заказ 12345 был успешно обработан

order_service_sms = OrderService(sms_notifier)
order_service_sms.process_order(
    "12346"
)  # Выведет: Отправка SMS: Уведомление: заказ 12346 был успешно обработан
