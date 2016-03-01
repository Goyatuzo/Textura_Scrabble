import unittest

from suffix import Suffix


class TestPrefix(unittest.TestCase):

    def test_construct(self):
        """Test constructor of Words."""
        suffix = Suffix(['hello'])
        self.assertEqual(suffix.data, ['olleh'])

    def test_get_operator(self):
        """Obtain the list of words that contain a prefix. Uses the [] operator."""
        suffix = Suffix(['hello', 'hi', 'jello'])

        self.assertEqual(suffix['lo'], ['hello', 'jello'])
        self.assertEqual(suffix['j'], [])

    def test_get_exception(self):
        """Using the __getitem__ operator (the [] operator) and inputting a number
        should raise a ValueError."""
        suffix = Suffix(['hi'])

        self.assertRaises(ValueError, suffix.__getitem__, 0)

if __name__ == '__main__':
    unittest.main()
