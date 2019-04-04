"""
Tests for movies.py
"""
import pytest

from src.movies import load_movies, mean_rating, best_rated


@pytest.fixture(scope='class')
def movies():
    return load_movies()


class TestLoadMovies:

    def test_it_should_return_a_list(self, movies):
        assert isinstance(movies, list), "Your function should return a list"

    def test_it_should_return_a_list_of_lists(self, movies):
        assert all([isinstance(m, list) for m in movies])

    def test_it_sublist_should_be_of_len_4(self, movies):
        assert all([len(m) == 3 for m in movies]), (
            "Your nested sublists should be of length 3")


class TestMeanRating:

    def test_returns_a_float(self):
        res = mean_rating()
        assert isinstance(res, float)

    def test_mean_rating(self):
        res = mean_rating()
        assert res == 8.258


class TestMostRated:

    def test_it_should_return_a_string(self):
        res = best_rated()
        assert isinstance(res, str)

    def test_best_rated(self):
        res = best_rated()
        assert res == "The Shawshank Redemption"
