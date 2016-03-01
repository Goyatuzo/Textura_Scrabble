import unittest

from words import Words


class TestWords(unittest.TestCase):

    @staticmethod
    def construct_word_list():
        """The word list that should be used by all tests."""
        return Words(['a', 'ab', 'b', 'ba', 'baa', 'genes'])

    def test_constructor(self):
        words = self.construct_word_list()

        expected = {
            'a': ['a'],
            'aab': ['baa'],
            'ab': ['ab', 'ba'],
            'b': ['b'],
            'eegns': ['genes']
        }

        self.assertEqual(words.data, expected)

    def test_letters_one(self):
        """Test the find_letters method by searching for one letter."""
        words = self.construct_word_list()

        # a should return 1.
        self.assertEquals(words.find_letters('a'), ['a'])
        # ab should return 2.
        self.assertEqual(words.find_letters('ab'), ['a', 'ab', 'b', 'ba'])
        # d should return 0.
        self.assertEquals(words.find_letters('d'), [])

    def test_letters_two(self):
        """Test the find_letters method by searching for a string
        of letters."""
        words = self.construct_word_list()

        # ab should return 4.
        self.assertEquals(words.find_letters('ab'), ['a', 'ab', 'b', 'ba'])
        self.assertEquals(words.find_letters('az'), ['a'])

    def test_get_exception(self):
        """Test that passing in an invalid value to the [] operator raises an error."""
        words = self.construct_word_list()

        self.assertRaises(ValueError, words.__getitem__, 0)
        self.assertRaises(ValueError, words.__getitem__, [])

    def test_get_item(self):
        """Test the [] operator for valid inputs."""
        words = self.construct_word_list()

        ab = ['a', 'ab', 'b', 'ba']

        self.assertEquals(words['a'], ['a'])
        # Should have all a b, but shouldn't have baa
        self.assertEquals(words['ba'], ab)
        self.assertEquals(words['ab'], ab)
        self.assertNotEqual(words['ab'], ab.extend(['baa']))

if __name__ == '__main__':
    unittest.main()
