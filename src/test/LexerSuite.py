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
        self.assertTrue(TestLexer.test("123abc", "Error Token 123abc", 118))
    
    def test_comment(self):
        """test comments"""
        self.assertTrue(TestLexer.test("## This is a comment", "## This is a comment,<EOF>", 119))
        self.assertTrue(TestLexer.test("## This is comment 1 \n ## This is comment 2", "## This is comment 1,## This is comment 2,<EOF>", 120))
        self.assertTrue(TestLexer.test("## This is comment 1 ### \n ## This is ## comment 2", "## This is comment 1 ###,## This is ## comment 2,<EOF>", 121))
        self.assertTrue(TestLexer.test("abc ## This is comment 1 ### \n ## This is ## comment 2", "abc,## This is comment 1 ###,## This is ## comment 2,<EOF>", 122))
        self.assertTrue(TestLexer.test("## This is comment 1 ### \n abc ## This is ## comment 2", "## This is comment 1 ###,abc,## This is ## comment 2,<EOF>", 123))
        self.assertTrue(TestLexer.test("## This is comment 1 ### \n ## This is ## comment 2 \n abc", "## This is comment 1 ###,## This is ## comment 2,abc,<EOF>", 124))
        self.assertTrue(TestLexer.test("1.2e10 abc## This is comment 1 ### \n ## This is ## comment 2 \n abc", "1.2e10,abc,## This is comment 1 ###,## This is ## comment 2,abc,<EOF>", 125))
        self.assertTrue(TestLexer.test("1.2E-10 cde## This is comment 1 ### \n ## This is ## comment 2 \n abc", "1.2E-10,cde,## This is comment 1 ###,## This is ## comment 2,abc,<EOF>", 126))
    
    def test_invalid_float_with_exp(self):
        """test invalid float with exp"""
        self.assertTrue(TestLexer.test("12e","Error Token 12e", 127))
        self.assertTrue(TestLexer.test("12E","Error Token 12E", 128))
        self.assertTrue(TestLexer.test("12.e","Error Token 12.e", 129))
        self.assertTrue(TestLexer.test("12.E","Error Token 12.E", 130))
    
    def test_identifiers(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc Abc aBC ABC abc_ \n ABC", "abc,Abc,aBC,ABC,abc_,\n,ABC,<EOF>", 131))
        self.assertTrue(TestLexer.test("_abcc_ \n ABC", "_abcc_,\n,ABC,<EOF>", 132))
        self.assertTrue(TestLexer.test("abcAbcaBCABCabc_\nABC", "abcAbcaBCABCabc_,\n,ABC,<EOF>", 133))
        self.assertTrue(TestLexer.test("\n\n ABC", "\n,\n,ABC,<EOF>", 134))
        self.assertTrue(TestLexer.test("\n\n\nabc Abc aBC ABC abc_ \n ABC", "\n,\n,\n,abc,Abc,aBC,ABC,abc_,\n,ABC,<EOF>", 135))
    
    def test_numbers(self):
        """test numbers"""
        self.assertTrue(TestLexer.test("1 2. 3 4.5 1.2e10 \n", "1,2.,3,4.5,1.2e10,\n,<EOF>", 136))
        self.assertTrue(TestLexer.test("1.e 10", "Error Token 1.e", 137))
        self.assertTrue(TestLexer.test("1.2 \n 2. e ", "1.2,\n,2.,e,<EOF>", 138))
        self.assertTrue(TestLexer.test("0.2 E 10", "0.2,E,10,<EOF>", 139))
        self.assertTrue(TestLexer.test("1.e-2 1e- 2", "1.e-2,Error Token 1e-", 140))
        self.assertTrue(TestLexer.test("1.a-2 1e-2", "Error Token 1.a-2", 141))
        self.assertTrue(TestLexer.test("1.Z+2 1e-2", "Error Token 1.Z+2", 142))
        self.assertTrue(TestLexer.test("1.Z+2 1e-2", "Error Token 1.Z+2", 142))
    

