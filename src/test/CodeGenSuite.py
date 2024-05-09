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
        
 #       input = """func main ()
 #       begin
 #           var a <- readNumber()
 #           writeNumber(a * 0)
 #       end
 #       """
 #       expect = "0.0"
 #       self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_bool(self):
        input = """func main ()
        begin
            writeBool(true)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

#        input = """func main ()
#        begin
#            bool a <- readBool()
#            writeBool(a or true)
#        end
#        """
#        expect = "true"
#        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_string(self):
        input = """func main ()
        begin
            writeString("Hello world!")
        end
        """
        expect = "Hello world!"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
  #      input = """func main ()
  #      begin
  #          var a <- readString()
  #      end
  #      """
  #      expect = ""
  #      self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_assign(self):
        input = """func main ()
        begin
            var a <- 4
            var b <- a
            var c <- b
            dynamic d
            d <- c
            writeNumber(a)
            writeNumber(b)
            writeNumber(c)
            writeNumber(d)
        end
        """
        expect = "4.04.04.04.0"
        self.assertTrue(TestCodeGen.test(input, expect, 506))
        
        input = """func main ()
        begin
            var a <- "anhuy"
            var b <- a
            string c <- b
            dynamic d
            d <- c
            writeString(a)
            writeString(b)
            writeString(c)
            writeString(d)
        end
        """
        expect = "anhuyanhuyanhuyanhuy"
        self.assertTrue(TestCodeGen.test(input, expect, 507))


