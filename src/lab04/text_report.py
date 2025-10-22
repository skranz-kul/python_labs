from collections import Counter
import os, sys
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.text import tokenize, normalize



def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)

new_str = read_text("data/samples/input.txt")


def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens) 

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

sorted_list = sorted_word_counts(frequencies_from_text(new_str))
maxi = 0
for i in sorted_list:
    maxi = max(maxi, len(i[0]))
len_razdelitel = (maxi // 2 + 1 if maxi % 2 == 0 else maxi // 2 + 2)
print('word', ' ' * len_razdelitel,'count')
for i in sorted_list:
    print(i[0], ' ' * ((len_razdelitel // 4 - 1 if len(i[0]) == maxi else len_razdelitel) if maxi % 3 != 0 else (len_razdelitel // 4 if len(i[0]) == maxi else len_razdelitel)), i[1])