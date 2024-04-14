import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_no_entry_point(self):
        input = """number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_no_body(self):
        input = """
            func f()
            func main() begin
            end
        """
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 401))

        input = """
            func f()
            func main() begin
                number f <- f()
            end
        """
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_forward_decl(self):
        input = """
            func f()
            func main() begin
                number f <- f()
            end
            func f() return 3
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 403))

        input = """
            func f()
            func main() begin
                number f <- f()
            end
            func f() return "abc"
        """
        expect = "Type Mismatch In Statement: Return(StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 404))

        input = """
            func f()
            func main() begin
                number f <- f()
            end
            func f() return f
        """
        expect = "Undeclared Identifier: f"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_conflicting_return_types(self):
        input = """
            func f()
            func main() begin
                number f <- f()
                number a <- f()
                string g <- f()
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(g), StringType, None, CallExpr(Id(f), []))"
        self.assertTrue(TestChecker.test(input, expect, 406))

        input = """
            func f() begin
                if (true)
                    return false
                else
                    return 2
            end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 407))

        input = """
            func f() begin
                if (true)
                    return false
                else
                    return "string"
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 408))

        input = """
            func f() begin
                if (true)
                    return false
                elif (false)
                    return "string"
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 409))

        input = """
            func f() begin
                if (true)
                    return false
                elif (false)
                    return true
                elif (true)
                    return "string"
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 410))

        input = """
            func f() begin
                if (true)
                    return false
                elif (false)
                    return true
                elif (true)
                    return true
                else
                    return "string"
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 411))

        input = """
            func f() begin
                if (true)
                    return false
                elif (false)
                    return true
                elif (true)
                    return false
                return 3
            end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 412))

        input = """
            func f() begin
                if (true)
                    return false
                elif (false)
                    return true
                elif (true)
                    return false
                return true
                begin
                    return 3
                end
            end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 413))

        input = """
            func f() begin
                if (true)
                    return false
                elif (false)
                    return true
                elif (true)
                    return false
                return true
                begin
                    return true
                    return 3
                end
            end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 414))

        input = """
            func f() begin
                begin
                    return true
                end
                if (true) begin
                    var a <- 3
                    return false
                end
                elif (false)
                    return true
                elif (true)
                    return false
                return 3
            end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 415))

        input = """
            func f() begin
                var a <- 3
                begin
                    return true
                end
                if (true) begin
                    return false
                end
                elif (false)
                    return true
                elif (true)
                    return false
                return a
            end
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 416))

        input = """
            func f() begin
                var a <- 3
                var b <- a
                begin
                    return true
                end
                if (true) begin
                    return false
                end
                elif (false)
                    return true
                elif (true)
                    return false
                return b
            end
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 417))

        input = """
            func f() begin
                var a <- 3
                var b <- a
                begin
                    return true
                end
                if (true) begin
                    return false
                end
                elif (false)
                    return true
                elif (true)
                    return false
                return true
                for a until a = 10 by 1
                    return b
            end
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 418))

        input = """
            func f() begin
                var a <- 3
                var b <- a
                begin
                    return true
                end
                if (true) begin
                    return false
                end
                elif (false)
                    return true
                elif (true)
                    return false
                return true
                for a until a = 10 by 1
                    return
            end
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 419))

        input = """
            func g()
            func f() begin
                var a <- 3
                var b <- a
                begin
                    return true
                end
                if (true) begin
                    return false
                end
                elif (false)
                    return true
                elif (true)
                    return false
                return true
                for a until a = 10 by 1
                    return true
                return g()
            end
        """
        expect = "No Function Definition: g"
        self.assertTrue(TestChecker.test(input, expect, 420))

        input = """
            func g()
            func f() begin
                var a <- 3
                var b <- a
                begin
                    return true
                end
                if (true) begin
                    return false
                end
                elif (false)
                    return true
                elif (true)
                    return false
                return true
                for a until a = 10 by 1
                    return true
                return g()
            end

            func g() return 3
        """
        expect = "Type Mismatch In Statement: Return(NumLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 421))

        input = """
            func g() begin
                return 3
            end
            func f() begin
                var a <- 3
                var b <- a
                begin
                    return true
                end
                if (true) begin
                    return false
                end
                elif (false)
                    return true
                elif (true)
                    return false
                return true
                for a until a = 10 by 1
                    return true
                return g()
            end
        """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(g), []))"
        self.assertTrue(TestChecker.test(input, expect, 422))

        input = """
            dynamic c
            func f() begin
                c <- 3
                var a <- 3
                begin
                    return true
                end
                if (true) begin
                    return false
                end
                elif (false)
                    return true
                elif (true)
                    return false
                return true
                for a until a = 10 by 1
                    return true
                begin
                    return c
                end
            end
        """
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_expressions(self):
        input = """
            number b <- a
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 424))

        input = """
            var a <- "string"
            number b <- a
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), NumberType, None, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 425))

        input = """
            var a <- "string"
            var b <- a ... " two string"

            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 426))

        input = """
            var a <- "string"
            var b <- (a ... 1) ... "two string"

            func main() begin
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., Id(a), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 427))

        input = """
            var a <- "string"
            var b <- (a ... [1]) ... "two string"

            func main() begin
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., Id(a), ArrayLit(NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 428))

        input = """
            dynamic a
            var b <- a ... "two string"

            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 429))

        input = """
            var a <- 3
            var b <- a + "string" + 3
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 430))

        input = """
            var a <- "string"
            var b <- a + 3 + "string"
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), NumLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 431))

        input = """
            var a <- "string"
            bool b <- a == "string"

            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))

        input = """
            var a <- 3
            bool b <- 3 = a

            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 433))

        input = """
            var a <- 3
            number b <- 3 + a

            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 434))

        input = """
            var a <- 3
            number b <- 3 + a

            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))

        input = """
            var a <- 3
            number b <- 3 - a

            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))

        input = """
            var a <- 3
            number b <- -2 * a

            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))

        input = """
            var a <- 3
            number b <- (3 - 2) / a

            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))

        input = """
            var a <- 3
            number b <- 3 * -a

            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))

        input = """
            var a <- 3
            bool b <- 3 > -a

            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 440))

        input = """
            var a <- 3
            bool b <- 3 >= -a

            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 441))

        input = """
            var a <- 3
            bool b <- 3 < -a

            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))

        input = """
            var a <- 3
            bool b <- 3 <= -a

            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))

        input = """
            var a <- 3
            bool b <- 3 = -a

            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 444))

        input = """
            var a <- 3
            bool b <- not true
            bool c <- not a

            func main() begin
            end
        """
        expect = "Type Mismatch In Expression: UnaryOp(not, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 445))

        input = """
            var a <- 1
            var b <- "1"
            var c <- true
            dynamic d

            func f() begin
                d <- (1 = a) and ("1" == b) or c
                return true
                return d
            end

            func main() begin
                bool f <- f()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_inference(self):
        input = """
            dynamic e
            dynamic d

            func f() begin
                d <- e ... "2"
                return d
            end

            func main() begin
                var a <- f()
                string d <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 447))

        input = """
            dynamic e
            dynamic d

            func f() begin
                if (d)
                    return e
                else begin
                    d <- false
                    return 3
                end
            end

            func main() begin
                bool d <- true
                number e <- f()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 448))

        input = """
            dynamic e
            dynamic d

            func f() begin
                if (d)
                    return e
                else begin
                    d <- 4
                    return 3
                end
            end

            func main() begin
                bool d <- true
                number e <- f()
            end
        """
        expect = "Type Mismatch In Expression: AssignStmt(Id(d), NumLit(4.0))"
        self.assertTrue(TestChecker.test(input, expect, 449))