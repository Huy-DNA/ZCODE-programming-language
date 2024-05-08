import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_number(self):
        input = """func main ()
        begin
            writeNumber(1)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 500))
        
        input = """func main ()
        begin
            var a <- readNumber()
            writeNumber(a * 0)
        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 501))
