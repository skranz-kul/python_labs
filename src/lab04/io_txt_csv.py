from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Функция для чтения текста из файла в одну строку
    для выбора другой кодировки нужно передать значение аргумента в функцию
    пример:
    read_text("Ваш_путь", "cp1251") - в данном случае кодировка будет cp1251 вместо utf-8
    """
    p = Path(path)
    return ''.join(p.read_text(encoding=encoding).split())

print(read_text("data/samples/input.txt"))

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """
    Функция для создания/перезаписывания csv
    есть проверка на длину строк на входе
    """
    p, rows = Path(path), list(rows)
    for i in range(len(rows) - 1): 
        # print(len(rows[i]), len(rows[i + 1]), rows[i], rows[i + 1])
        if len(rows[i]) != len(rows[i + 1]): raise ValueError
    with p.open("w", newline='', encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None: w.writerow(header)
        for r in rows: w.writerow(r)
write_csv([("word","count"),("test",3)], "src/lab04/output.csv", 'ddg') 
# write_csv(rows=[], path="src/lab04/output.csv", header=None)