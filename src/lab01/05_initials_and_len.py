full = input("ФИО: ")

trimmed = full.strip()
parts = [p for p in trimmed.split() if p]

initials = "".join(part[0].upper() for part in parts) + "."

print(f"Инициалы: {initials}")
length_without_spaces = len("".join(trimmed.split()))
print(f"Длина (символов): {length_without_spaces}")

