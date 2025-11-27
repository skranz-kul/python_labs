import sys
from pathlib import Path

lib_path = Path(__file__).parent.parent / "lib"
sys.path.insert(0, str(lib_path))

from text import tokenize, normalize, count_freq, top_n


def read_stdin_text() -> str:
    return sys.stdin.read()


def print_stats(total_count: int, unique_count: int, top_items):
    print(f"Всего слов: {total_count}")
    print(f"Уникальных слов: {unique_count}")
    print("Топ-5:")
    for word, count in top_items:
        print(f"{word}:{count}")


def main():
    raw_text = read_stdin_text()
    normalized = normalize(raw_text)
    tokens = tokenize(normalized)
    freq_map = count_freq(tokens)
    leaders = top_n(freq_map, 5)
    print_stats(len(tokens), len(set(tokens)), leaders)


if __name__ == "__main__":
    main()
