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

        input = """func main ()
        begin
            var a <- true
            var b <- a
            bool c <- b
            dynamic d
            d <- c
            writeBool(a)
            writeBool(b)
            writeBool(c)
            writeBool(d)
        end
        """
        expect = "truetruetruetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_assign_across_scope(self):
        input = """
        dynamic a1
        var a2 <- 4
        string a3 <- "anhuy"
        func main ()
        begin
            a1 <- false
            var a <- a1
            number b <- a2 
            string c <- a3
            writeBool(a)
            writeNumber(b)
            writeString(c)
        end
        """
        expect = "false4.0anhuy"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

        input = r"""
        func main ()
        begin
            dynamic a1
            var a2 <- 4
            string a3 <- "anhuy"
            begin
                a1 <- false
                var a2 <- 5
                var a3 <- "huyan"
                writeBool(a1)
                writeNumber(a2)
                writeString(a3)
            end
            writeString("\n")
            writeBool(a1)
            writeNumber(a2)
            writeString(a3)
        end
        """
        expect = "false5.0huyan\nfalse4.0anhuy"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_function_definitions(self):
        input = r"""
        func f()
        func main ()
        begin
            number a <- f()
            writeNumber(a)
            writeNumber(f())
        end
        func f() return 2
        """
        expect = "2.02.0"
        self.assertTrue(TestCodeGen.test(input, expect, 511))
        
        input = r"""
        func f()
        func main ()
        begin
            bool a <- f()
            writeBool(a)
            writeBool(f())
        end
        func f() return true
        """
        expect = "truetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

        input = r"""
        func f()
        func main ()
        begin
            string a <- f()
            writeString(a)
            writeString(f())
        end
        func f() return "anhuy"
        """
        expect = "anhuyanhuy"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_if(self):
        input = r"""
        func main ()
        begin
            if (false)
                writeString("NO")
            else writeString("YES")
        end
        """
        expect = "YES"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

        input = r"""
        func main ()
        begin
            if (true)
                writeString("NO")
            else writeString("YES")
        end
        """
        expect = "NO"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

        input = r"""
        func main ()
        begin
            if (1 + 1 != 2)
                writeString("1 + 1 != 2")
            elif (2 + 2 = 3)
                writeString("2 + 2 = 3")
            elif (1 + 3 != 4)
                writeString("1 + 3 != 4")
            elif (1 + 3 = 4)
                writeString("1 + 3 = 4")
            else
                writeString("???")
        end
        """
        expect = "1 + 3 = 4"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

        input = r"""
        func main ()
        begin
            if (1 + 1 != 2)
                writeString("1 + 1 != 2")
            elif (2 + 2 = 3)
                writeString("2 + 2 = 3")
            elif (1 + 3 != 4)
                writeString("1 + 3 != 4")
            elif ((1 + 3 = 4) and (1 + 1 = 3))
                writeString("1 + 3 = 4 and 1 +1 = 3")
            else
                writeString("???")
        end
 
        """
        expect = "???"
        self.assertTrue(TestCodeGen.test(input, expect, 517))
        
    def test_for(self): 
        input = r"""
        dynamic x
        func main ()
        begin
            x <- 0
            for x until x = 10 by 1 begin
                writeNumber(x)
                writeString(" ")
            end
        end
 
        """
        expect = "0.0 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 "
        self.assertTrue(TestCodeGen.test(input, expect, 518))
        
        input = r"""
        dynamic x
        func main ()
        begin
            x <- 0
            for x until x > 10 by 1 * 0 + 2 begin
                writeNumber(x)
                writeString(" ")
            end
        end
 
        """
        expect = "0.0 2.0 4.0 6.0 8.0 10.0 "
        self.assertTrue(TestCodeGen.test(input, expect, 519))

        input = r"""
        dynamic x
        func main ()
        begin
            x <- 0
            for x until true by 1 begin
                writeNumber(x)
                writeString(" ")
            end
        end
 
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 520))
        
    def test_expression(self): 
        input = r"""
        func main ()
        begin
            var x <- (1 + 1) * 2
            var y <- x * x
            var z <- y / x
            var t <- y % 3
            var r <- z + t
            writeNumber(r)
        end
 
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

        input = r"""
        func main ()
        begin
            var x <- 0
            for x until x = 5 by 1
                writeNumber(x % 2)
        end
        """
        expect = "0.01.00.01.00.0"
        self.assertTrue(TestCodeGen.test(input, expect, 522))
        
        input = r"""
        func main ()
        begin
            var x <- 0
            var str <- "huy"
            var str2 <- ""
            for x until x = 2 by 1 begin
                str <- str ... str
                str2 <- str2 ... "huy"
            end
            writeString(str)
            writeString("\n")
            writeString(str2)
        end
        """
        expect = "huyhuyhuyhuy\nhuyhuy"
        self.assertTrue(TestCodeGen.test(input, expect, 523))
        
        input = r"""
        func getArr() return [1,2,3,4]
        dynamic numArr 
        func main ()
        begin
            numArr <- getArr()
            var x <- 0
            for x until x = 4 by 1
                writeNumber(numArr[x])
        end
        """
        expect = "1.02.03.04.0"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

        input = r"""
        func getArr() return ["an", "huy"]
        dynamic strArr 
        func main ()
        begin
            strArr <- getArr()
            var x <- 0
            for x until x = 2 by 1
                writeString(strArr[x])
        end
        """
        expect = "anhuy"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

        input = r"""
        func getArr() return [true, false]
        dynamic boolArr 
        func main ()
        begin
            boolArr <- getArr()
            var x <- 0
            for x until x = 2 by 1
                writeBool(boolArr[x])
        end
        """
        expect = "truefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

        input = r"""
        func getArr() return [["an", " "], ["huy", "."]]
        dynamic strArr 
        func main ()
        begin
            strArr <- getArr()
            var x <- 0
            for x until x = 2 by 1
            begin
                var y <- 0
                for y until y = 2 by 1
                    writeString(strArr[x, y])
            end
        end
        """
        expect = "an huy."
        self.assertTrue(TestCodeGen.test(input, expect, 527))

        input = r"""
        func getArr() return [[[0]], [[1]], [[2]]]
        dynamic numArr 
        func main ()
        begin
            numArr <- getArr()
            var x <- 0
            for x until x = 3 by 1
            begin
                var y <- 0
                for y until y = 1 by 1
                begin
                    var z <- 0
                    for z until z = 1 by 1
                        writeNumber(numArr[x][y, z])
                end
            end
        end
        """
        expect = "0.01.02.0"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_break_and_continue(self):
        input = r"""
        func main ()
        begin
            var x <- 0
            for x until x = 10 by 1
            begin
                if (x = 2.0) begin
                    break
                end
                writeNumber(x)
            end
        end
        """
        expect = "0.01.0"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

        input = r"""
        func main ()
        begin
            var x <- 0
            for x until x = 10 by 1
            begin
                if (x % 2 = 0) begin
                    continue
                end
                writeNumber(x)
            end
        end
        """
        expect = "1.03.05.07.09.0"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

        input = r"""
        func main ()
        begin
            var x <- 0
            for x until x = 10 by 1
            begin
                if (x % 2 = 0) begin
                    continue
                end
                if (x % 5 = 0) begin
                    break
                end
                writeNumber(x)
            end
        end
        """
        expect = "1.03.0"
        self.assertTrue(TestCodeGen.test(input, expect, 531))
 
        input = r"""
        func main ()
        begin
            var x <- 0
            for x until x = 10 by 1
            begin
                if ((x % 2 = 0) or (x % 3 = 0)) begin
                    continue
                end
                if (x % 7 = 0) begin
                    break
                end
                writeNumber(x)
            end
        end
        """
        expect = "1.05.0"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

        input = r"""
        func main ()
        begin
            var x <- 0
            for x until x = 10 by 1
            begin
                if ((x % 2 = 0) or (x % 3 = 0)) begin
                    if (x % 6 = 0)
                        break
                    continue
                end
                writeNumber(x)
            end
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 533))

        input = r"""
        func main ()
        begin
            var x <- 0
            for x until x = 3 by 1
            begin
                var y <- 0
                for y until y = 3 by 1
                begin
                    if (x + y = 2)
                        break
                    writeNumber(x)
                    writeString(":")
                    writeNumber(y)
                    writeString("-")
                end
            end
        end
        """
        expect = "0.0:0.0-0.0:1.0-1.0:0.0-"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_boolean_expressions(self):
        input = r"""
        func main ()
        begin
            writeBool(true and true) 
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

        input = r"""
        func main ()
        begin
            writeBool(true and false) 
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

        input = r"""
        func main ()
        begin
            writeBool(false and true) 
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

        input = r"""
        func main ()
        begin
            writeBool(false and false) 
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

        input = r"""
        func main ()
        begin
            writeBool(true or true) 
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

        input = r"""
        func main ()
        begin
            writeBool(false or true) 
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

        input = r"""
        func main ()
        begin
            writeBool(true or false) 
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

        input = r"""
        func main ()
        begin
            writeBool(false or false) 
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 542))



