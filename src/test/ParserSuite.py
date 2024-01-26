import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_return_function(self):
        """Function with simple return body"""
        input = """func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    
    def test_block_function(self):
        """Function with body as block"""
        input = """func main ()
        begin
            return 1 + 2
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_block_function_with_comment(self):
        """Function with body as block and comment"""
        input = """func main () ## This is the main function
        ## This is before the body
        begin
            ## This is the body
            return "abc'""
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_return_function_with_comment(self):
        """Function with body as return and comment"""
        input = """func main () ## This is the main function
        ## This is before the body
        

        return 100
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_func_decl_with_comment(self):
        """Function declaration with comment"""
        input = """func main () ## This is the main function
        ## This is after the decl
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    
    def test_func_decl(self):
        """Function declaration"""
        input = """func main ()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_expr(self):
        self.assertTrue(TestParser.test("1 + 2 * 3", "successful",207))
        self.assertTrue(TestParser.test("1 / 2 * 3", "successful",208))
        self.assertTrue(TestParser.test("1 - 2 / 3", "successful",209))
        self.assertTrue(TestParser.test("1 + 2 or 3", "successful",210))
        self.assertTrue(TestParser.test("(1 + 2) or (3 and 4)", "successful",211))
        self.assertTrue(TestParser.test("1 + 2 ... 3 + 5", "successful",212))
        self.assertTrue(TestParser.test("a = b = c", "Error on line 1 col 6: =",213))
        self.assertTrue(TestParser.test("a % 2 = 0 or b % 2 = 0", "Error on line 1 col 19: =",214))
        self.assertTrue(TestParser.test("a = (b = c)", "successful",215))
        self.assertTrue(TestParser.test("a ... b ... c", "Error on line 1 col 8: ...",216))
        self.assertTrue(TestParser.test("(a ... b) ... c", "successful",217))
        self.assertTrue(TestParser.test("(a % 2 = 0) or (b % 2 = 0)", "successful",218))
        self.assertTrue(TestParser.test("a < b < c", "Error on line 1 col 6: <",219))
        self.assertTrue(TestParser.test("a > b > c", "Error on line 1 col 6: >",220))
        self.assertTrue(TestParser.test("a != b != c", "Error on line 1 col 7: !=",221))
        self.assertTrue(TestParser.test("a >= b >= c", "Error on line 1 col 7: >=",222))
        self.assertTrue(TestParser.test("a <= b <= c", "Error on line 1 col 7: <=",223))
        self.assertTrue(TestParser.test("a <= b >= c", "Error on line 1 col 7: >=",224))
        self.assertTrue(TestParser.test("a == b == c", "Error on line 1 col 7: ==",225))
        self.assertTrue(TestParser.test("a == b >= c", "Error on line 1 col 7: >=",226))
        self.assertTrue(TestParser.test("a <= b >= c", "Error on line 1 col 7: >=",227))
        self.assertTrue(TestParser.test("a = b <= c", "Error on line 1 col 6: <=",228))