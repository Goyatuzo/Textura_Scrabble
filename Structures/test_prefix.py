import unittest

from prefix import Prefix


class TestPrefix(unittest.TestCase):

    def test_construct(self):
        """Test constructor of Words."""
        prefix = Prefix()
        self.assertEqual(prefix.data, [])

        prefix = Prefix(['T'])
        self.assertEqual(prefix.data, ['T'])

    def test_add_basic(self):
        """Test adding one entry into data structure."""
        prefix = Prefix()
        prefix.add('Hello')

        expected = [
            'Hello'
        ]

        self.assertEqual(prefix.data, expected)

    def test_add_multiple(self):
        """Test adding multiple entries into the data structure. They
        should be in alphabetical order even though they were added
        randomly."""
        prefix = Prefix()
        prefix.add('Test')
        prefix.add('Pass')

        expected = [
            'Pass',
            'Test'
        ]

        self.assertEqual(prefix.data, expected)

    def test_add_collision(self):
        """Test adding two values that share common characters."""
        prefix = Prefix()
        prefix.add('H')
        prefix.add('He')

        expected = [
            'H',
            'He'
        ]

        self.assertEqual(prefix.data, expected)

    def test_get_simple(self):
        """Obtain the list of words that contain a prefix. Uses the simple algorithm."""
        prefix = Prefix()
        prefix.add('absolute')
        prefix.add('abstinent')
        prefix.add('best')
        prefix.add('tab')

        self.assertEqual(prefix.get_words_simple('ab'), ['absolute', 'abstinent'])

    def test_get_operator(self):
        """Obtain the list of words that contain a prefix. Uses the [] operator."""
        prefix = Prefix()
        prefix.add('absolute')
        prefix.add('abstinent')
        prefix.add('best')
        prefix.add('tab')

        self.assertEqual(prefix['ab'], ['absolute', 'abstinent'])

    def test_get_exception(self):
        """Using the __getitem__ operator (the [] operator) and inputting a number
        should raise a ValueError."""
        prefix = Prefix()
        prefix.add('Hi')

        self.assertRaises(ValueError, prefix.__getitem__, 0)

if __name__ == '__main__':
    unittest.main() 
