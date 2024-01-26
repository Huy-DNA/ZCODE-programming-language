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
        """Function with body as block"""
        input = """func main () ## This is the main function
        ## This is before the body
        begin
            ## This is the body
            return "abc'""
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))