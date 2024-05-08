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

    def test_bool(self):
        input = """func main ()
        begin
            writeBool(true)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

        input = """func main ()
        begin
            bool a <- readBool()
            writeBool(a or true)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_string(self):
        input = """func main ()
        begin
            writeString("Hello world!")
        end
        """
        expect = "Hello world!"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
        input = """func main ()
        begin
            var a <- readString()
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 505))


