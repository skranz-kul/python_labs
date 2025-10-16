def normalize(input_text: str, *, apply_casefold: bool = True, yo_to_e: bool = True) -> str:
    if input_text == "": return ""
    if apply_casefold: 
        input_text = input_text.casefold()
    if yo_to_e:
        input_text = input_text.replace("ё","е").replace("Ё","Е")
    input_text = " ".join(input_text.split())
    return input_text
"""
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
print("#"*18)
print(" "*18)
"""
def tokenize(input_text: str) -> list[str]:
    tokens = []
    current_chunk = []
    for char in input_text+" ":
        if char.isalnum() or char == "_":
            current_chunk.append(char)
        elif char == "-" and len(current_chunk)>=1 and current_chunk[-1].isalnum():
            current_chunk.append(char)        
        else:
            if len(current_chunk) >=1:   
                tokens.append("".join(current_chunk))
                current_chunk = []
    return tokens 
"""
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
print("#"*10)
print(" "*10)
"""
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq_map = {}
    for token in tokens:
        freq_map[token] = freq_map.get(token,0) +1
    return freq_map
"""
print(count_freq(["a","b","a","c","b","a"]))
print("#"*10)
print(" "*10) 
"""
def top_n(freq_map: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = list(freq_map.items())
    sorted_items.sort(key = lambda item: (-item[1],item[0]))
    return sorted_items[:n]
# print(top_n({"bb":2,"aa":2,"cc":3}))