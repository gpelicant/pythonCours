"""
Tests for counter module
"""
import pytest

try:
    from src.counter import Counter
    imported = True
except ImportError:
    imported = False


def test_class_counter_should_be_defined():
    assert imported, "Did you define the Counter class?"


def test_it_should_init_with_an_empty_count_values():
    counter = Counter()
    assert counter.values == {}


def test_it_should_create_missing_keys():
    counter = Counter()
    counter.count('num_lines')
    assert 'num_lines' in counter.values.keys()


def test_it_should_increment_missing_keys():
    counter = Counter()
    counter.count('num_lines', 1)
    assert counter.values['num_lines'] == 1


def test_default_value_is_1():
    counter = Counter()
    counter.count('num_lines')
    assert counter.values['num_lines'] == 1


def test_default_value_is_1_bis():
    counter = Counter()
    counter.count('num_lines')
    counter.count('num_lines')
    assert counter.values['num_lines'] == 2


@pytest.mark.parametrize("counts", [
    [0, 0], [1, 1], [3, 3], [1, 3, 6], [1, -3], [-1, 3]
])
def test_it_should_increment_and_decrement_existing_keys(counts):
    counter = Counter()
    for c in counts:
        counter.count('num_lines', c)
    assert counter.values['num_lines'] == sum(counts)
