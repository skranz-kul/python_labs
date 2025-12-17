import pytest
from pathlib import Path
from src.lab09.group import Group
from src.lab08.models import Student


def test_init_creates_file(tmp_path: Path):
    """тест: создание файла при инициализации, если его нет"""
    csv_path = tmp_path / "students.csv"
    group = Group(str(csv_path))
    
    assert csv_path.exists()
    assert csv_path.read_text(encoding="utf-8").startswith("fio,birthdate,group,gpa")


def test_init_validates_existing_header(tmp_path: Path):
    """тест: проверка корректного заголовка в существующем файле"""
    csv_path = tmp_path / "students.csv"
    csv_path.write_text("fio,birthdate,group,gpa\n", encoding="utf-8")
    
    group = Group(str(csv_path))
    assert group.path == csv_path


def test_init_invalid_header(tmp_path: Path):
    """тест: ошибка при неверном заголовке"""
    csv_path = tmp_path / "students.csv"
    csv_path.write_text("name,age\n", encoding="utf-8")
    
    with pytest.raises(ValueError, match="неверный заголовок CSV"):
        Group(str(csv_path))


def test_list_empty(tmp_path: Path):
    """тест: список пуст для нового файла"""
    csv_path = tmp_path / "students.csv"
    group = Group(str(csv_path))
    
    students = group.list()
    assert students == []


def test_add_and_list(tmp_path: Path):
    """тест: добавление студента и получение списка"""
    csv_path = tmp_path / "students.csv"
    group = Group(str(csv_path))
    
    student = Student(
        fio="Иванов Иван Иванович",
        birthdate="2000-01-15",
        group="ИСП-201",
        gpa=4.5
    )
    
    group.add(student)
    students = group.list()
    
    assert len(students) == 1
    assert students[0].fio == "Иванов Иван Иванович"
    assert students[0].group == "ИСП-201"
    assert students[0].gpa == 4.5


def test_add_multiple(tmp_path: Path):
    """тест: добавление нескольких студентов"""
    csv_path = tmp_path / "students.csv"
    group = Group(str(csv_path))
    
    student1 = Student("Петров Петр", "2001-02-20", "ИСП-201", 4.0)
    student2 = Student("Сидоров Сидор", "2002-03-25", "ИСП-202", 3.5)
    
    group.add(student1)
    group.add(student2)
    
    students = group.list()
    assert len(students) == 2
    assert students[0].fio == "Петров Петр"
    assert students[1].fio == "Сидоров Сидор"


def test_find_by_substring(tmp_path: Path):
    """тест: поиск студентов по подстроке"""
    csv_path = tmp_path / "students.csv"
    group = Group(str(csv_path))
    
    group.add(Student("Иванов Иван", "2000-01-15", "ИСП-201", 4.5))
    group.add(Student("Петров Петр", "2001-02-20", "ИСП-201", 4.0))
    group.add(Student("Иванова Мария", "2002-03-25", "ИСП-202", 3.5))
    
    found = group.find("Иванов")
    assert len(found) == 2
    assert all("Иванов" in s.fio for s in found)


def test_find_case_insensitive(tmp_path: Path):
    """тест: поиск без учёта регистра"""
    csv_path = tmp_path / "students.csv"
    group = Group(str(csv_path))
    
    group.add(Student("Иванов Иван", "2000-01-15", "ИСП-201", 4.5))
    
    found = group.find("иванов")
    assert len(found) == 1
    assert found[0].fio == "Иванов Иван"


def test_find_no_results(tmp_path: Path):
    """тест: поиск несуществующего студента"""
    csv_path = tmp_path / "students.csv"
    group = Group(str(csv_path))
    
    group.add(Student("Иванов Иван", "2000-01-15", "ИСП-201", 4.5))
    
    found = group.find("Сидоров")
    assert len(found) == 0


def test_remove(tmp_path: Path):
    """тест: удаление студента"""
    csv_path = tmp_path / "students.csv"
    group = Group(str(csv_path))
    
    group.add(Student("Иванов Иван", "2000-01-15", "ИСП-201", 4.5))
    group.add(Student("Петров Петр", "2001-02-20", "ИСП-201", 4.0))
    
    group.remove("Иванов Иван")
    
    students = group.list()
    assert len(students) == 1
    assert students[0].fio == "Петров Петр"


def test_remove_multiple_same_fio(tmp_path: Path):
    """тест: удаление всех записей с одинаковым ФИО"""
    csv_path = tmp_path / "students.csv"
    group = Group(str(csv_path))
    
    # добавляем дубликаты (хотя в реальности это странно)
    student = Student("Иванов Иван", "2000-01-15", "ИСП-201", 4.5)
    group.add(student)
    group.add(student)
    
    group.remove("Иванов Иван")
    
    students = group.list()
    assert len(students) == 0


def test_update(tmp_path: Path):
    """тест: обновление полей студента"""
    csv_path = tmp_path / "students.csv"
    group = Group(str(csv_path))
    
    group.add(Student("Иванов Иван", "2000-01-15", "ИСП-201", 4.5))
    
    group.update("Иванов Иван", gpa=5.0, group="ИСП-202")
    
    students = group.list()
    assert len(students) == 1
    assert students[0].gpa == 5.0
    assert students[0].group == "ИСП-202"
    assert students[0].fio == "Иванов Иван"


def test_update_nonexistent(tmp_path: Path):
    """тест: ошибка при обновлении несуществующего студента"""
    csv_path = tmp_path / "students.csv"
    group = Group(str(csv_path))
    
    with pytest.raises(ValueError, match="студент с ФИО"):
        group.update("Несуществующий", gpa=5.0)


def test_update_invalid_field(tmp_path: Path):
    """тест: ошибка при обновлении несуществующего поля"""
    csv_path = tmp_path / "students.csv"
    group = Group(str(csv_path))
    
    group.add(Student("Иванов Иван", "2000-01-15", "ИСП-201", 4.5))
    
    with pytest.raises(ValueError, match="неизвестное поле"):
        group.update("Иванов Иван", invalid_field="value")


def test_update_invalid_data(tmp_path: Path):
    """тест: ошибка при обновлении с некорректными данными"""
    csv_path = tmp_path / "students.csv"
    group = Group(str(csv_path))
    
    group.add(Student("Иванов Иван", "2000-01-15", "ИСП-201", 4.5))
    
    with pytest.raises(ValueError):
        group.update("Иванов Иван", gpa=10.0)  # gpa должен быть от 0 до 5


def test_read_all_validates_data(tmp_path: Path):
    """тест: валидация данных при чтении"""
    csv_path = tmp_path / "students.csv"
    csv_path.write_text(
        "fio,birthdate,group,gpa\n"
        "Иванов Иван,2000-01-15,ИСП-201,4.5\n"
        "Петров Петр,invalid-date,ИСП-201,4.0\n",
        encoding="utf-8"
    )
    
    group = Group(str(csv_path))
    
    with pytest.raises(ValueError, match="некорректные данные"):
        group.list()


def test_read_all_validates_missing_field(tmp_path: Path):
    """тест: валидация отсутствующих полей"""
    csv_path = tmp_path / "students.csv"
    csv_path.write_text(
        "fio,birthdate,group,gpa\n"
        "Иванов Иван,2000-01-15,ИСП-201\n",  # отсутствует gpa
        encoding="utf-8"
    )
    
    group = Group(str(csv_path))
    
    with pytest.raises(ValueError, match="отсутствует поле"):
        group.list()


