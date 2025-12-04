from dataclasses import dataclass
from datetime import datetime, date
from typing import Dict, Any


@dataclass
class Student:
    """
    класс для представления студента
    декоратор @dataclass для автоматической генерации
    методов __init__ и других
    """
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        """
        метод вызывается автоматически после __init__
        используется для валидации данных после создания объекта
        """
        # дата
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                f"Неверный формат даты: {self.birthdate}. "
                f"Ожидается формат YYYY-MM-DD"
            )
        # средний балл
        if not (0 <= self.gpa <= 5):
            raise ValueError(
                f"Средний балл должен быть в диапазоне от 0 до 5, "
                f"получено: {self.gpa}"
            )

    def age(self) -> int:
        """
        вычисляет и возвращает количество полных лет студента
        """
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age_years = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age_years -= 1
        return age_years

    def to_dict(self) -> Dict[str, Any]:
        """
        сериализует объект Student в словарь
        возвращает словарь со всеми полями класса
        """
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, pasd: Dict[str, Any]) -> "Student":
        """
        десериализует словарь в объект Student
        это classmethod, поэтому вызывается через класс: Student.from_dict(dict)
        """
        # создаётся новый экземпляр класса, используя значения из словаря
        return cls(
            fio=pasd["fio"],
            birthdate=pasd["birthdate"],
            group=pasd["group"],
            gpa=pasd["gpa"],
        )

    def __str__(self) -> str:
        """
        возвращает строковое представление объекта для пользователя 
        вызывается при использовании str() или print()
        """
        return f"студент: {self.fio}, группа: {self.group}, GPA: {self.gpa}, возраст: {self.age()}"

