import json
from typing import List
from .models import Student


def students_to_json(students: List[Student], path: str) -> None:
    """
    cериализует список объектов student в JSON-файл
    """
    data = [student.to_dict() for student in students]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> List[Student]:
    """
    Десериализует JSON-файл в список объектов Student.
    
    Args:
        path: Путь к JSON-файлу для чтения
        
    Returns:
        Список объектов Student
    """
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    students = [Student.from_dict(d) for d in data]
    return students
