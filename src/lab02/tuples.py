def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple) or len(rec) != 3:
        return "TypeError"

    fio, group, gpa = rec

    if not isinstance(fio, str):
        return "TypeError"
    if not isinstance(group, str):
        return "TypeError"
    if not isinstance(gpa, (int, float)):
        return "TypeError"
    fio_parts = fio.strip().split()
    if not fio_parts:
        return "ValueError"
    if len(fio_parts) < 2:
        return "ValueError"
    if not group.strip():
        return "ValueError"
    surname = fio_parts[0].capitalize()
    initials = []
    for name_part in fio_parts[1:]:
        if name_part:
            initials.append(name_part[0].upper() + ".")
    formatted_fio = surname + " " + "".join(initials)
    result = f"{formatted_fio}, гр. {group.strip()}, GPA {gpa:.2f}"
    return result


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("", "BIVT-25", 4.6)))
print(format_record(("Иванов", "BIVT-25", 4.6)))
print(format_record(("Иванов Иван", "", 4.6)))
print(format_record(("Иванов Иван", "BIVT-25", "4.6")))
