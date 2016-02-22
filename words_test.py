import unittest
from words import Words

class TestWordsMethods(unittest.TestCase):

    def test_construct(self):
        wordList = Words()
        self.assertEqual(wordList.data, {})

    def test_add_basic(self):
        wordList = Words()
        wordList.add('Hello')

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

        self.assertEqual(wordList.data, expected)

if __name__ == '__main__':
    unittest.main() 
