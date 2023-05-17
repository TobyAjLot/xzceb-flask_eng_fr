import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """Tests the functions in translator module"""

    def test_english_text(self):
        """Tests funnction englishText in translator module"""
        self.assertIsNotNone(english_to_french('NotNull'))
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_frenchText(self):
        """Tests funnction frenchText in translator module"""
        self.assertIsNotNone(french_to_english('NotNull'))
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main()