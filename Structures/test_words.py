import unittest

from words import Words


class TestWords(unittest.TestCase):

    @staticmethod
    def construct_word_list():
        """The word list that should be used by all tests."""
        return Words(['a', 'ab', 'b', 'back', 'zen'])

    def test_letters_one(self):
        """Test the find_letters method by searching for one letter."""
        words = self.construct_word_list()

        # a should return 3.
        self.assertEquals(words.find_letters('a'), ['a', 'ab', 'back'])
        # z should return 1.
        self.assertEquals(words.find_letters('z'), ['zen'])
        # d should return 0.
        self.assertEquals(words.find_letters('d'), [])

    def test_letters_two(self):
        """Test the find_letters method by searching for a string
        of letters."""
        words = self.construct_word_list()

        # ab should return 4.
        self.assertEquals(words.find_letters('ab'), ['a', 'ab', 'b', 'back'])
        self.assertEquals(words.find_letters('az'), ['a', 'ab', 'back', 'zen'])

    def test_get_exception(self):
        """Test that passing in an invalid value to the [] operator raises an error."""
        words = self.construct_word_list()

        self.assertEquals(words['ab'], ['a', 'ab', 'b', 'back'])
        self.assertEquals(words['az'], ['a', 'ab', 'back', 'zen'])
        self.assertRaises(ValueError, words.__getitem__, 0)
        self.assertRaises(ValueError, words.__getitem__, [])

if __name__ == '__main__':
    unittest.main()
