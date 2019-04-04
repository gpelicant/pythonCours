"""
Tests
"""
from os import path

import pytest

from src.data import load_data


INPUT_PATH = path.join('..', 'input')

FILENAME = 'la_classe.txt'


def test_it_should_load_data_when_file_exists():
    res = load_data(path.join(INPUT_PATH, FILENAME))
    assert res is not None


def test_it_should_print_when_file_does_not_exist(capsys):
    load_data('unknown_file.txt')
    out, _ = capsys.readouterr()
    assert out.rstrip() == "Logging: file does not exist..."
