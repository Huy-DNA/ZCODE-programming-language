import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_simple_string(self):
        """test simple string"""
        self.assertTrue(TestLexer.test("\"Yanxi Palace - 2018\"","\"Yanxi Palace - 2018\",<EOF>",101))

    def test_complex_string(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("\"isn\\'t\"","\"isn\\'t\",<EOF>",102))
    
    def test_unclose_string(self):
        """test unclose string"""
        self.assertTrue(TestLexer.test("\"abc", "Unclosed String: \"abc", 103))
    
    def test_invalid_escape(self):
        """test invalid escape"""
        self.assertTrue(TestLexer.test("\"abc \\v\"", "Illegal Escape In String: \"abc \\v\"", 104))

    def test_valid_escape(self):
        """test valid escape"""
        self.assertTrue(TestLexer.test("\"abc \\f\"", "\"abc \\f\",<EOF>", 105))