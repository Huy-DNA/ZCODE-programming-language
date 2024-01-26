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