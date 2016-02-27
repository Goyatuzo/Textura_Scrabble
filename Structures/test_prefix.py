import unittest

from prefix import Prefix


class TestPrefix(unittest.TestCase):

    def test_construct(self):
        """Test constructor of Words."""
        prefix = Prefix()
        self.assertEqual(prefix.data, {})

    def test_add_basic(self):
        """Test adding one entry into data structure."""
        prefix = Prefix()
        prefix.add('Hello')

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

        self.assertEqual(prefix.data, expected)

    def test_add_multiple(self):
        """Test adding multiple entries into the data structure."""
        prefix = Prefix()
        prefix.add('Test')
        prefix.add('Pass')

        expected = {
            'T': {
                'e': {
                    's': {
                        't': {
                            ' ': {}
                        }
                    }
                }
            },
            'P': {
                'a': {
                    's': {
                        's': {
                            ' ': {}
                        }
                    }
                }
            }
        }

        self.assertEqual(prefix.data, expected)

    def test_add_collision(self):
        """Test collision adding in the data structure. They should
        share the same path until the part where the words separate."""
        prefix = Prefix()
        prefix.add('H')
        prefix.add('He')

        expected = {
            'H': {
                ' ': {},
                'e': {
                    ' ': {}
                }
            }
        }

        self.assertEqual(prefix.data, expected)

    def test_exist_basic(self):
        """Test the existence method for one single entry."""
        prefix = Prefix()
        prefix.add('Hello')

        # Hello should exist, but Hell should not.
        self.assertTrue(prefix.exists('Hello'))
        self.assertFalse(prefix.exists('Hell'))
        self.assertFalse(prefix.exists('Hello '))

    def test_exist_multiple(self):
        """Test the existence method for multiple entries."""
        prefix = Prefix()
        prefix.add('Te')
        prefix.add('He')

        # Assert Te exists, but not T.
        self.assertTrue(prefix.exists('Te'))
        self.assertFalse(prefix.exists('T'))

        # Assert He exists, but not just e.
        self.assertTrue(prefix.exists('He'))
        self.assertFalse(prefix.exists('e'))

    def test_exist_collision(self):
        """This one has a collision where the common root is the capital H. Make
        sure that H and He both exist."""
        prefix = Prefix()
        prefix.add('H')
        prefix.add('He')

        # Only H and He should exist. Check for case sensitivity.
        self.assertTrue(prefix.exists('H'))
        self.assertFalse(prefix.exists('h'))
        self.assertTrue('He')

if __name__ == '__main__':
    unittest.main() 
