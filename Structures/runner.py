# Test runner example taken from
# http://stackoverflow.com/questions/1732438/how-to-run-all-python-unit-tests-in-a-directory

import unittest

test_modules = [
    'test_prefix',
    'test_words'
]

suite = unittest.TestSuite()

for t in test_modules:
    try:
        # If the module defines a suite() function, call it to get the suite.
        mod = __import__(t, globals(), locals(), ['suite'])
        suite_fn = getattr(mod, 'suite')
        suite.addTest(suite_fn())
    except (ImportError, AttributeError):
        # else, just load all the test cases from the module.
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)
