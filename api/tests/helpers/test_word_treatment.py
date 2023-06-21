import unittest
from api.helpers.word_treatment import vowel_count, sort_words, validate_words


class TestFunctions(unittest.TestCase):

    def setUp(self) -> None:
        self.words = ["banana", "apple", "cherry", "date"]

    def test_vowel_count(self):
        words = self.words
        expected_result = {
            "banana": 3,
            "apple": 2,
            "cherry": 1,
            "date": 2
        }
        result = vowel_count(words)
        self.assertEqual(result, expected_result)

    def test_sort_words_asc(self):
        words = self.words

        # Test ascending order
        order = "asc"
        expected_result_asc = ["banana", "apple", "cherry", "date"]
        result_asc = sort_words(words, order)
        self.assertEqual(result_asc, expected_result_asc)

    def test_sort_words_desc(self):
        words = self.words
        # Test descending order
        order = "desc"
        expected_result_desc = ['date', 'cherry', 'apple', 'banana']
        result_desc = sort_words(words, order)
        self.assertEqual(result_desc, expected_result_desc)

    def test_validate_words_list_with_integer(self):
        # Valid list of strings
        value = self.words
        result = validate_words(value)
        self.assertEqual(result, value)

        # Invalid list (not all strings)
        value = ["banana", "apple", 123, "date"]
        with self.assertRaises(ValueError):
            validate_words(value)

        # Invalid value (not a list)
        value = "banana"
        with self.assertRaises(ValueError):
            validate_words(value)
