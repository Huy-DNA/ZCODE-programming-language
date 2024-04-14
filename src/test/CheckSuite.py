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