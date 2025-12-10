import csv
from pathlib import Path
from typing import List
from src.lab08.models import Student


class Group:
    """
    класс для управления группой студентов, хранящейся в CSV-файле
    """
    
    REQUIRED_HEADER = ["fio", "birthdate", "group", "gpa"]
    
    def __init__(self, storage_path: str):
        """
        инициализация группы и файла хранилища
        
        args:
            storage_path: путь к CSV-файлу с данными студентов
        """
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self) -> None:
        """
        создать файл с заголовком, если его ещё нет
        проверяет наличие крректного заголовка в существующем файле
        """
        if not self.path.exists():
            # создаём файл с заголовком
            with self.path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self.REQUIRED_HEADER)
                writer.writeheader()
        else:
            # проверяем, что заголовок корректный
            with self.path.open("r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                if reader.fieldnames != self.REQUIRED_HEADER:
                    raise ValueError(
                        f"неверный заголовок CSV. ожидается: {self.REQUIRED_HEADER}, "
                        f"получено: {reader.fieldnames}"
                    )
    
    def _read_all(self) -> List[dict]:
        """
        прочитать все строки из CSV.
        
        returns:
            список словарей с данными студентов

        raises:
            valueError: если данные не соответствуют формату student
        """
        rows = []
        with self.path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            # проверяем заголовок
            if reader.fieldnames != self.REQUIRED_HEADER:
                raise ValueError(
                    f"неверный заголовок CSV. ожидается: {self.REQUIRED_HEADER}, "
                    f"получено: {reader.fieldnames}"
                )
            
            for row_num, row in enumerate(reader, start=2):  # start=2, т.к. строка 1 - заголовок
                # валидация: проверяем, что все поля присутствуют и не пустые
                for field in self.REQUIRED_HEADER:
                    if field not in row or row[field] is None or (isinstance(row[field], str) and row[field].strip() == ""):
                        raise ValueError(
                            f"строка {row_num}: отсутствует поле '{field}'"
                        )
                
                # валидация: проверяем, что можно создать объект student
                try:
                    row["gpa"] = float(row["gpa"])
                    # пробуем создать student для валидации
                    Student.from_dict(row)
                except (ValueError, KeyError, TypeError) as e:
                    raise ValueError(
                        f"строка {row_num}: некорректные данные - {e}"
                    )
                
                rows.append(row)
        
        return rows
    
    def list(self) -> List[Student]:
        """
        вернуть всех студентов в виде списка student.
        
        returns:
            список объектов student
        """
        rows = self._read_all()
        return [Student.from_dict(row) for row in rows]
    
    def add(self, student: Student) -> None:
        """
        добавить нового студента в CSV.
        
        args:
            student: объект student для добавления
        """
        # валидация происходит автоматически при создании student
        student_dict = student.to_dict()
        
        with self.path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.REQUIRED_HEADER)
            writer.writerow(student_dict)
    
    def find(self, substr: str) -> List[Student]:
        """
        найти студентов по подстроке в fio.
        
        args:
            substr: подстрока для поиска в поле fio
            
        returns:
            список найденных студентов
        """
        rows = self._read_all()
        matching_rows = [r for r in rows if substr.lower() in r["fio"].lower()]
        return [Student.from_dict(row) for row in matching_rows]
    
    def remove(self, fio: str) -> None:
        """
        удалить запись(и) с данным fio.
        
        args:
            fio: полное ФИО для удаления
        """
        rows = self._read_all()
        # удаляем все записи с данным fio
        rows = [r for r in rows if r["fio"] != fio]
        
        # перезаписываем файл
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.REQUIRED_HEADER)
            writer.writeheader()
            writer.writerows(rows)
    
    def update(self, fio: str, **fields) -> None:
        """
        обновить поля существующего студента.
        
        args:
            fio: ФИО студента для обновления
            **fields: поля для обновления (fio, birthdate, group, gpa)
        """
        rows = self._read_all()
        updated = False
        
        for row in rows:
            if row["fio"] == fio:
                # обновляем поля
                for key, value in fields.items():
                    if key not in self.REQUIRED_HEADER:
                        raise ValueError(f"неизвестное поле: {key}")
                    row[key] = value
                
                # валидация: проверяем, что обновлённые данные корректны
                try:
                    row["gpa"] = float(row["gpa"])
                    Student.from_dict(row)
                except (ValueError, KeyError) as e:
                    raise ValueError(f"некорректные данные после обновления: {e}")
                
                updated = True
                break
        
        if not updated:
            raise ValueError(f"студент с ФИО '{fio}' не найден")
        
        # перезаписываем файл
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.REQUIRED_HEADER)
            writer.writeheader()
            writer.writerows(rows)

