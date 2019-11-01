import unittest

class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        pass

    ## Return True if the string contains 4 a.
    def test_strings_001(self):
        self.assertEqual( 'a'*4, 'aaaa')

    ## Returns True if the string is in upper case.
    def test_strings_002(self):
        self.assertEqual('foo'.upper(), 'FOO')

    ## Returns True if the string is in uppercase else returns False
    def test_strings_003(self):
        self.assertTrue('FOO'.isupper())
#        self.assertFalse('FOO'.isupper())


if __name__ == '__main__':
    unittest.main()

