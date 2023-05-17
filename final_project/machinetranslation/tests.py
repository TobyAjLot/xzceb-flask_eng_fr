import unittest

from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    """Tests the functions in translator module"""

    def test_english_text(self):
        """Tests funnction englishText in translator module"""

        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('NotEqual'), 'Bonjour')

    def test_french_text(self):
        """Tests funnction frenchText in translator module"""
        
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('NotEqual'), 'Hello')


if __name__ == '__main__':
    unittest.main()