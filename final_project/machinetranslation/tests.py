import unittest
from translator import englishToFrench, frenchToEnglish
class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(englishToFrench('Hello'), 'Oui')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  
        
class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(frenchToEnglish('Oui'), 'Hello')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')  
        
unittest.main()