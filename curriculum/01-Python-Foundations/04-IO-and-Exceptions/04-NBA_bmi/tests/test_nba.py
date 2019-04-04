"""
Tests
"""
import pytest

from src.nba import load_data, extract_height, bmi_pounds_inches as bmi


@pytest.fixture
def data():
    return load_data()


class TestBMI:

    def test_bmi(self):
        assert bmi(0, 1) == 0

    @pytest.mark.parametrize("height, weight, expected_bmi", [
        (250, 80, 27.46),
        (195, 75, 24.37),
        (184, 73, 24.27)
    ])
    def test_bmi_default_value(self, height, weight, expected_bmi):
        assert bmi(height, weight) == expected_bmi

    @pytest.mark.parametrize("height, weight, round_value, expected_bmi", [
        (250, 80, 2, 27.46),
        (195, 75, 0, 24),
        (184, 73, 3, 24.273)
    ])
    def test_bmi_non_default(self, height, weight, round_value, expected_bmi):
        assert bmi(height, weight, round_=round_value) == expected_bmi


class TestExtractHeight:

    @pytest.mark.parametrize("height_string", [
        ("6-8", ),
        ("6-3", ),
    ])
    def test_return_an_integer(self, height_string):
        res = extract_height(height_string)
        assert isinstance(res, int)

    def test_returns_0_if_invalid_string(self):
        res = extract_height("foobar")
        assert res == 0, "If the string is 'invalid' it should return 0"


    @pytest.mark.parametrize("height_string, expected_bmi", [
        ("6-8", 80),
        ("6-3", 75),
    ])
    def test_base(self, height_string, expected_bmi):
        assert extract_height(height_string) == expected_bmi


class TestLoadData:

    def test_it_returns_a_tuple(self, data):
        assert isinstance(data, tuple)

    def test_first_object_is_weights(self, data):
        weights, _ = data
        assert isinstance(weights[0], int)

    def test_it_returns_lists_with_equal_lengths(self, data):
        weights, heights = data
        assert len(weights) == len(heights)
