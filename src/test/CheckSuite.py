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