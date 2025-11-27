import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("   ", ""),
        ("Один", "один"),
        ("МНОГО\t\t\tПРОБЕЛОВ\n\n\n", "много пробелов"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
        ("   ", []),
        ("word1_word2", ["word1_word2"]),
        ("test-test", ["test-test"]),
        ("a-b-c", ["a-b-c"]),
        ("-неправильно", ["неправильно"]),
        ("правильно-", ["правильно"]),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        ([], {}),
        (["word"], {"word": 1}),
        (["a", "a", "a"], {"a": 3}),
        (["one", "two", "three"], {"one": 1, "two": 1, "three": 1}),
    ],
)
def test_count_freq_basic(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize(
    "freq_map, n, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, 2, [("a", 3), ("b", 2)]),
        ({"a": 3, "b": 2, "c": 1}, 5, [("a", 3), ("b", 2), ("c", 1)]),
        ({"word": 1}, 1, [("word", 1)]),
        ({}, 5, []),
        ({"a": 1, "b": 1, "c": 1}, 2, [("a", 1), ("b", 1)]),
    ],
)
def test_top_n_basic(freq_map, n, expected):
    assert top_n(freq_map, n) == expected


def test_top_n_tie_breaker():
    """Проверка сортировки по алфавиту при равных значениях частоты"""
    freq_map = {"bb": 2, "aa": 2, "cc": 3, "dd": 2}
    result = top_n(freq_map, 4)
    assert result == [("cc", 3), ("aa", 2), ("bb", 2), ("dd", 2)]


def test_top_n_all_same_frequency():
    """Все слова с одинаковой частотой - сортировка по алфавиту"""
    freq_map = {"zebra": 1, "apple": 1, "banana": 1}
    result = top_n(freq_map, 3)
    assert result == [("apple", 1), ("banana", 1), ("zebra", 1)]


def test_top_n_default_n():
    """Проверка значения по умолчанию n=5"""
    freq_map = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
    result = top_n(freq_map)
    assert len(result) == 5
    assert result[0] == ("f", 6)
