"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    position = 'engineer'
    _income = {"wage": 24000, "bonus": 8000}
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')
    def get_total_income(self):
        print(self._income.get("wage") + self._income.get("bonus"))


m_1= Position('alex', 'Ivanov')
m_2 = Position('Pit', 'Larsen')
m_1.get_full_name()
m_1.get_total_income()
m_2.get_full_name()
m_2.get_total_income()