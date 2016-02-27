import unittest

from prefix import Prefix


class TestPrefix(unittest.TestCase):

    def test_construct(self):
        """Test constructor of Words."""
        word_list = Prefix()
        self.assertEqual(word_list.data, {})

    def test_add_basic(self):
        """Test adding one entry into data structure."""
        word_list = Prefix()
        word_list.add('Hello')

        expected = {
            'H': {
                'e': {
                    'l': {
                        'l': {
                            'o': {
                                ' ': {}
                            }
                        }
                    }
                }
            }
        }

        self.assertEqual(word_list.data, expected)

    def test_add_multiple(self):
        """Test adding two entries into the data structure. The two
        entries have common letters so there should be one dictionary
        with multiple entries."""
        word_list = Prefix()
        word_list.add('H')
        word_list.add('He')

        expected = {
            'H': {
                ' ': {},
                'e': {
                    ' ': {}
                }
            }
        }

        self.assertEqual(word_list.data, expected)

    def test_exist_basic(self):
        """Test the existence method for one single entry."""
        word_list = Prefix()
        word_list.add('Hello')

        # Hello should exist, but Hell should not.
        self.assertTrue(word_list.exists('Hello'))
        self.assertFalse(word_list.exists('Hell'))
        self.assertFalse(word_list.exists('Hello '))

    def test_exist_multiple(self):
        """Test the existence method for multiple entries. This one
        also has a collision where the common root is the capital H."""
        word_list = Prefix()
        word_list.add('H')
        word_list.add('He')

        # Only H and He should exist. Check for case sensitivity.
        self.assertTrue(word_list.exists('H'))
        self.assertFalse(word_list.exists('h'))
        self.assertTrue('He')

if __name__ == '__main__':
    unittest.main() 
