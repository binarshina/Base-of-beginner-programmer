from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Оплата {amount} выполнена с помощью кредитной карты.")


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Оплата {amount} выполнена через PayPal.")


def make_payment(processor, amount):
    processor.process_payment(amount)


make_payment(CreditCardProcessor(), 100)
make_payment(PayPalProcessor(), 200)
