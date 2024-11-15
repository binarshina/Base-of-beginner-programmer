from abc import ABC, abstractmethod


# Низкоуровневая реализация
class FileWriter:
    def write_to_file(self, data: str) -> None:
        print(f"Writing to file: {data}")


# Высокоуровневая логика
class ReportGenerator:
    def __init__(self) -> None:
        self.file_writer = FileWriter()  # Прямое создание конкретного класса

    def generate(self, report: str) -> None:
        self.file_writer.write_to_file(report)


# Пример использования
report_generator = ReportGenerator()
report_generator.generate("My Report Data")
