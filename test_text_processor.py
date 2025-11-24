#import module
#from file import class
import pytest
from text_processor import TextProcessor

#python -m pytest .\test_text_processor.py -v

def test_capitalize_text_equal():
    """1. Assert equal - egyenlőség ellenőrzés"""
    processor = TextProcessor()
    result = processor.capitalize_text("haló")
    assert result == "HALÓ"
    #assert result == "HALó" rossz teszt példa


def test_capitalize_text_not_equal():
    """2. Assert not equal - nem egyenlő"""
    processor = TextProcessor()
    result = processor.capitalize_text("haló")
    assert result != "HALÓ!"
    assert result != "GND"


def test_reverse_text_in():
    """3. Assert in - benne van"""
    processor = TextProcessor()
    result = processor.reverse_text("haló")
    #assert "o" in result rossz teszt példa
    assert "a" in result


def test_reverse_text_not_in():
    """4. Assert not in - nincs benne"""
    processor = TextProcessor()
    result = processor.reverse_text("haló")
    #assert "o" not in result #rossz teszt példa
    #assert "a" not in result
    assert "x" not in result


def test_count_words_isinstance():
    """5. Assert isinstance - típus ellenőrzés"""
    processor = TextProcessor()
    result = processor.count_words("Ez egy teszt.")
    assert isinstance(result, int)
    assert not isinstance(result, str)
    assert isinstance(result, float) is False
    assert isinstance(result, (int, float))


def test_count_words_greater_less():
    """6. Assert >, <, >=, <= - összehasonlítás"""
    processor = TextProcessor()
    result1 = processor.count_words("Helló")
    result2 = processor.count_words("Helló világ")
    result3 = processor.count_words("Helló világ Python")
    assert result1 < result2
    assert result3 > result2
    assert result2 >= result1
    assert result1 <= result3

def test_count_words_empty_string():
    """7. Üres sztring bemenet ellenőrzése"""
    pass


def test_is_palindrome_true_false():
    """8. Assert True/False - boolean ellenőrzés"""
    pass


def test_remove_spaces_multiple_asserts():
    """9. Több assert egy tesztben"""
    pass