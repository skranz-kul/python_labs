import sys
import os
from pathlib import Path

lib_path = Path(__file__).parent.parent / 'lib'
sys.path.insert(0, str(lib_path))

from text import tokenize, normalize, count_freq, top_n


def read_stdin_text() -> str:
    return sys.stdin.read()


def _is_truthy_env(value: str | None) -> bool:
    if value is None:
        return False
    normalized = value.strip().lower()
    return normalized in {'1', 'true', 'yes', 'y', 'on'}


def _print_table(top_items):
    col_word = 'слово'
    col_freq = 'частота'
    max_word_width = max(len(col_word), *(len(word) for word, _ in top_items)) if top_items else len(col_word)
    header = f"{col_word:<{max_word_width}} | {col_freq}"
    separator = '-' * (max_word_width + 3 + len(col_freq))
    print(header)
    print(separator)
    for word, count in top_items:
        print(f"{word:<{max_word_width}} | {count}")


def print_stats(total_count: int, unique_count: int, top_items):
    print(f'Всего слов: {total_count}')
    print(f'Уникальных слов: {unique_count}')
    print('Топ-5:')
    if _is_truthy_env(os.getenv('TEXT_STATS_TABLE')):
        _print_table(top_items)
    else:
        for word, count in top_items:
            print(f'{word}:{count}')


def main():
    raw_text = read_stdin_text()
    normalized = normalize(raw_text)
    tokens = tokenize(normalized)
    freq_map = count_freq(tokens)
    leaders = top_n(freq_map, 5)
    print_stats(len(tokens), len(set(tokens)), leaders)


if __name__ == '__main__':
    main()