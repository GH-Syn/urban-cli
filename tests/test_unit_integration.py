import os
import sys
import unittest
import random

from bs4 import BeautifulSoup, NavigableString, Tag

sys.path.insert(0, os.getcwd())

from src.urban import (
    assert_soup_and_index_valid,
    get_found_word_from_soup,
    get_soup_object_from_word,
)


words = [
    "YOLO",
    "eshay",
    "swag",
    "gtfo",
    "lit",
    "rad",
    "hella",
    "joint",
    "block",
    "dope",
    "rickroll",
]


class TestUnitIntegration(unittest.TestCase):
    """Test functions working with other functions"""

    def setUp(self) -> None:
        try:
            self.word = random.choice(words)
            print(f"[{words.index(self.word)}] LOOKING UP: {self.word}")
            self.soup = get_soup_object_from_word(self.word)
        except IndexError:
            sys.exit(0)

    def test_word_from_soup_raises_index_error(self):
        """Test that word from soup raises when a given value is missing"""

        with self.assertRaises(IndexError):
            _soup = get_soup_object_from_word(self.word)
            word_soup = _soup.find_all_next("a")[0].select(  # pyright: ignore
                ".definintion"
            )  # pyright: ignore
            word_soup_raises_key_error = word_soup[0].replace_with(
                word_soup[0].get_text(strip=False)
            )

            assert_soup_and_index_valid(_soup)

            get_found_word_from_soup(
                BeautifulSoup(
                    word_soup_raises_key_error.get_text(strip=False), "html.parser"
                )
            )