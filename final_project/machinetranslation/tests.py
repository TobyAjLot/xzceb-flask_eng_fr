import unittest

from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    """Tests the functions in translator module"""

    def test_english_text(self):
        """Tests funnction englishText in translator module"""
        self.assertIsNotNone(englishToFrench('NotNull'))
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_frenchText(self):
        """Tests funnction frenchText in translator module"""
        self.assertIsNotNone(frenchToEnglish('NotNull'))
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main()