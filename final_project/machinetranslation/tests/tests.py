import unittest
from translator import englishToFrench, frenchToEnglish
  
class LanguageTranslatorTest(unittest.TestCase):
  
    # Returns True or False. 
    def test_englishToFrench_null(self):        
        self.assertEqual(englishToFrench(" "), " ")

    # Returns True or False. 
    def test_englishToFrench_Hello_Bonjour(self):        
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    # Returns True or False. 
    def test_englishToFrench_assertNotEqual(self):
        self.assertNotEqual(englishToFrench("Hello"), "Hello")
    
    # Returns True or False. 
    def test_frenchToEnglish_null(self):        
        self.assertEqual(frenchToEnglish(" "), " ")

    # Returns True or False. 
    def test_frenchToEnglish_Hello_Bonjour(self):        
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

    # Returns True or False. 
    def test_frenchToEnglish_assertNotEqual(self):
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Bonjour")
  
if __name__ == '__main__':
    unittest.main()