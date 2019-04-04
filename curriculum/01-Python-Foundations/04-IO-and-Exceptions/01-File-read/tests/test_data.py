"""
Tests
"""
from os import path
from unittest.mock import Mock, patch

import pytest

from src.data import load_data, file_stats


FILENAME = 'la_classe.txt'


FILE_DATA = (
    """Tu n'es vraiment pas très sympa. Mais le train de tes injures roule sur le rail de mon indifférence. Je préfère partir plutôt que d'entendre ça plutôt que d'être sourd.
    Attention, ce flim n’est pas un flim sur le cyclimse. Merci de votre compréhension.
    Excuse-moi de te dire ça, mon pauvre José, mais tu confonds un peu tout. Tu fais un amalgame entre la coquetterie et la classe. Tu es fou.
    Si tu veux me parler, envoie-moi un... fax !
    En tout cas s’il cherchait pour du trouble, il est venu à la bonne place.
    C’est ça, la puissance intellectuelle. Bac + 2, les enfants.
    Blablabla, j’ai les bonbons qui collent au papier.
    On va manger... des chips ! T'entends ?!? Des chips ! C'est tout ce que ça te
    fait quand je te dis qu'on va manger des chips ? Mais qu'est-ce qui t'arrive?
    Pourquoi tu dis rien, tu fais la tronche ou quoi?
    Parce que si on réfléchit bien, moi je suis un vrai démocrate. George est un fasciste de merde. Un fasciste de merde !"""
)



def test_load_data():
    # TODO: replace is a quick hack, neeeds fix
    res = load_data(path.join('input', FILENAME)).rstrip('\n').replace(" ", "")
    assert res == FILE_DATA.rstrip('\n').replace(" ", "")


class TestFileStats:

    def test_it_should_return_a_dict(self):
        res = file_stats(path.join('input', FILENAME))
        assert isinstance(res, dict), "You should return a dict"


    @pytest.mark.parametrize("key", [
        "num_lines", "num_words", "num_chars"
    ])
    def test_keys(self, key):
        res = file_stats(path.join('input', FILENAME))
        assert key in res.keys(), f"Make sure {f} is in your dict"

    @pytest.mark.parametrize("key, value", [
        ("num_lines", 11),
        ("num_words", 178),
        ("num_chars", 948)
    ])
    def test_num_lines(self, key, value):
        res = file_stats(path.join('input', FILENAME))
        assert res[key] == value, f"Wrong value for {key}"
