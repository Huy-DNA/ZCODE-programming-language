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
        self.assertTrue(TestParser.test("a...b", "successful", 229))
    
    def test_if(self):
        """If statement"""
        input = """
        if 3 5 ## This is a comment
        if (4) 5
        if (5) if (6) 5
        if 1 + 2 if 3 + 4 if 5 + 6 "abcd"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_elif(self):
        """If and elif statement"""
        input = """
        if 3 5 ## This is a comment
        elif (4) 5
        elif (5) 8 elif (6) 5
        if 1 + 2 if 3 + 4 if 5 + 6 10 elif "abcd" "aaaa" ... "bbbb"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_invalid_if(self):
        """Invalid if statement"""
        input = """
        if 3 ## This is a comment
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,232))

        input = """
        if 3 ## This is a comment
        if 5
        if 6 if 7
        """
        expect = "Error on line 5 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,233))

        input = """
        if ## This is a comment
        elif 10 5
        """
        expect = "Error on line 2 col 11: ## This is a comment"
        self.assertTrue(TestParser.test(input,expect,234))
 
        input = """
        if 3 ## This is a comment
        elif 10
        """
        expect = "Error on line 3 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,235))

        input = """
        if 3 5 ## This is a comment
        elif 10
        """
        expect = "Error on line 3 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,236))

        input = """
        if 3 5 ## This is a comment
        elif 10
        elif 8 3
        """
        expect = "Error on line 3 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,237))

        input = """
        if 3 ## This is a comment
        elif
        """
        expect = "Error on line 3 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,238))

        input = """
        if 3 ## This is a comment
        else
        """
        expect = "Error on line 3 col 8: else"
        self.assertTrue(TestParser.test(input,expect,239))

        input = """
        if 3 ## This is a comment
        elif 10
        else
        """
        expect = "Error on line 3 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,240))

        input = """
        if 3 ## This is a comment
        elif
        else
        """
        expect = "Error on line 3 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,241))

        input = """
        if
        elif
        else
        """
        expect = "Error on line 2 col 10: \n"
        self.assertTrue(TestParser.test(input,expect,242))
    
    def test_else(self):
        """Test else"""
        input = """
        if 3 10 ## This is a comment
        elif 5
            if 6 10
            elif 5 10
            else 10
        else 10
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))

        input = """
        if 3 ## 1
            if 5 ## 2
                if 6 ## 3
                    10 ## 4
                else 8 ## 5
        ## 6


        elif 5 ## 8
            if 6 10 ## 9
            elif 5 10 ## 10
            else 10 ## 11



        else
            if 10 10
            elif 10 10
            else 10
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_decl(self):
        """Test declaration"""
        input = """
            number a_ <- 1
            bool b <- true
            string _c_d_ <- "abc'""
            number a[4] <- [1,2,3,4]
            bool b[5] <- [true, false, true, false, true]
            string C1c[1] <- ["123"]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

        input = """
            type a_ <- 1
        """
        expect = "Error on line 2 col 17: a_"
        self.assertTrue(TestParser.test(input,expect,246))

        input = """
            number a_
            bool b
            string _c_d_
            number a[4,5,6]
            bool b[5,1]
            string C1c[1]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))

        input = """
            number a[4,[4]] <- [1,2,3,4]
        """
        expect = "Error on line 2 col 23: ["
        self.assertTrue(TestParser.test(input,expect,248))
 
        input = """
            number a[4,"Hello"] <- [1,2,3,4]
        """
        expect = "Error on line 2 col 23: \"Hello\""
        self.assertTrue(TestParser.test(input,expect,249))

        input = """
            number a[4,1+2] <- [1,2,3,4]
        """
        expect = "Error on line 2 col 24: +"
        self.assertTrue(TestParser.test(input,expect,250))

        input = """
            number a[] <- [1,2,3,4]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))

        input = """
            number a[1][1] <- [1,2,3,4]
        """
        expect = "Error on line 2 col 23: ["
        self.assertTrue(TestParser.test(input,expect,252))

        input = """
            number a[] <- [1,2,3,4]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))