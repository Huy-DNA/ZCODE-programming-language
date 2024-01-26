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
        self.assertTrue(TestLexer.test("\"abcd'\"", "Unclosed String: \"abcd'\"", 113))
    
    def test_invalid_escape(self):
        """test invalid escape"""
        self.assertTrue(TestLexer.test("\"abc \\v\"", "Illegal Escape In String: \"abc \\v\"", 104))

    def test_valid_escape(self):
        """test valid escape"""
        self.assertTrue(TestLexer.test("\"abc \\f\"", "\"abc \\f\",<EOF>", 105))
    
    def test_integer(self):
        """test integer"""
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 106))

    def test_float_with_no_decimal(self):
        """test floating point number with no decimal"""
        self.assertTrue(TestLexer.test("123.", "123.,<EOF>", 107))
    
    def test_float_with_decimal(self):
        """test floating point number with a decimal part"""
        self.assertTrue(TestLexer.test("123.456", "123.456,<EOF>", 108))

    def test_invalid_float_without_int(self):
        """test invalid floating point number without an integral part"""
        self.assertTrue(TestLexer.test(".456", "Error Token .", 109))

    def test_float_with_no_decimal_and_with_exp(self):
        """test valid floating point number without a decimal part but have an exponent part"""
        self.assertTrue(TestLexer.test("123.e456", "123.e456,<EOF>", 110))
        self.assertTrue(TestLexer.test("123e456", "123e456,<EOF>", 111))
    
    def test_full_float(self):
        """test full fledge floating point number"""
        self.assertTrue(TestLexer.test("123.456e789", "123.456e789,<EOF>", 112))

    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("a123", "a123,<EOF>", 114))
        self.assertTrue(TestLexer.test("A123", "A123,<EOF>", 115))
        self.assertTrue(TestLexer.test("AabC123", "AabC123,<EOF>", 116))
        self.assertTrue(TestLexer.test("_abC_123", "_abC_123,<EOF>", 117))
        self.assertTrue(TestLexer.test("123abc", "123,abc,<EOF>", 118))
    
    def test_comment(self):
        """test comments"""
        self.assertTrue(TestLexer.test("## This is a comment", "## This is a comment,<EOF>", 119))
        self.assertTrue(TestLexer.test("## This is comment 1 \n ## This is comment 2", "## This is comment 1,## This is comment 2,<EOF>", 120))
        self.assertTrue(TestLexer.test("## This is comment 1 ### \n ## This is ## comment 2", "## This is comment 1 ###,## This is ## comment 2,<EOF>", 121))
        self.assertTrue(TestLexer.test("abc ## This is comment 1 ### \n ## This is ## comment 2", "abc,## This is comment 1 ###,## This is ## comment 2,<EOF>", 122))
        self.assertTrue(TestLexer.test("## This is comment 1 ### \n abc ## This is ## comment 2", "## This is comment 1 ###,abc,## This is ## comment 2,<EOF>", 123))
        self.assertTrue(TestLexer.test("## This is comment 1 ### \n ## This is ## comment 2 \n abc", "## This is comment 1 ###,## This is ## comment 2,abc,<EOF>", 124))
        