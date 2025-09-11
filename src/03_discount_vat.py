def parse_number(text: str) -> float:
    return float(text.strip().replace(",", "."))


price = parse_number(input("price: "))
discount = parse_number(input("discount: "))
vat = parse_number(input("vat: "))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} ₽")
print(f"НДС:               {vat_amount:.2f} ₽")
print(f"Итого к оплате:    {total:.2f} ₽")


