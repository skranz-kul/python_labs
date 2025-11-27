def parse_number(text: str) -> float:
    text = text.strip().replace(",", ".")
    return float(text)


a_str = input("a: ")
b_str = input("b: ")

a = parse_number(a_str)
b = parse_number(b_str)

total = a + b
avg = total / 2

print(f"sum={total}; avg={avg}")
