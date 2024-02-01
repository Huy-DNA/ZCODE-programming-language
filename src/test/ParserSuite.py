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
        if (3) 5 ## This is a comment
        if (4) 5
        if (5) if (6) 5
        if (1 + 2) if (3 + 4) if (5 + 6) "abcd"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_elif(self):
        """If and elif statement"""
        input = """
        if (3) 5 ## This is a comment
        elif (4) 5
        elif (5) 8 elif (6) 5
        if (1 + 2) if (3 + 4) if (5 + 6) 10 elif ("abcd") "aaaa" ... "bbbb"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_invalid_if(self):
        """Invalid if statement"""
        input = """
        if (3) ## This is a comment
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,232))

        input = """
        if 3 ## This is a comment
        """
        expect = "Error on line 2 col 11: 3"
        self.assertTrue(TestParser.test(input,expect,233))

        input = """
        if ## This is a comment
        elif (10) 5
        """
        expect = "Error on line 2 col 11: ## This is a comment"
        self.assertTrue(TestParser.test(input,expect,234))
 
        input = """
        if (3) ## This is a comment
        elif (10)
        """
        expect = "Error on line 3 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,235))

        input = """
        if (3) 5 ## This is a comment
        elif (10)
        """
        expect = "Error on line 3 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,236))

        input = """
        if (3) 5 ## This is a comment
        elif (10)
        elif (8) 3
        """
        expect = "Error on line 3 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,237))

        input = """
        if (3) ## This is a comment
        elif
        """
        expect = "Error on line 3 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,238))

        input = """
        if (3) ## This is a comment
        else
        """
        expect = "Error on line 3 col 8: else"
        self.assertTrue(TestParser.test(input,expect,239))

        input = """
        if (3) ## This is a comment
        elif (10)
        else
        """
        expect = "Error on line 3 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,240))

        input = """
        if (3) ## This is a comment
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
        if (3) 10 ## This is a comment
        elif (5)
            if (6) 10
            elif (5) 10
            else 10
        else 10
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))

        input = """
        if (3) ## 1
            if (5) ## 2
                if (6) ## 3
                    10 ## 4
                else 8 ## 5
        ## 6


        elif (5) ## 8
            if (6) 10 ## 9
            elif (5) 10 ## 10
            else 10 ## 11



        else
            if (10) 10
            elif (10) 10
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
        expect = "Error on line 2 col 23: Hello"
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
        self.assertTrue(TestParser.test(input,expect,253))

        input = """
            var a
            number b <- 3
        """
        expect = "Error on line 2 col 17: \n"
        self.assertTrue(TestParser.test(input,expect,254))

        input = """
            var a <- 3
            var c <- "aaa'""
            var t <- true
            number b <- 3
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))

        input = """
            dynamic a <- 3
            dynamic c <- "aaa'""
            dynamic t <- true
            dynamic b
            b <- 3
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))

        input = """
            var a <- ### This a decl
            3
        """
        expect = "Error on line 2 col 21: ### This a decl"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_assignment(self):
        """Test assignment"""
        input = """
           a <- 3
           b <- "aaa" ... "bbb"
           c <- 1 + 2 + 3
           d <- 1 * 3 / 2 % true and false ... "abc" 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))

        input = """
            a <- ## This is a comment
            1 + 2
        """
        expect = "Error on line 2 col 17: ## This is a comment"
        self.assertTrue(TestParser.test(input,expect,259))

    def test_for(self): 
        input = """
            for i until 10 by 1
            ## 1212

            ### 1221


                a <- a + 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))

        input = """
            for a[i] until x + 10 by 2 begin
                b <- a[i]
                a <- x + 10
                if (a[i] % 3 == 0)
                    break
            end 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))

        input = """
            for f() until a[i] by 1 + 1
            ## 123
            ## 12212

            begin
                f()
                f()
                continue
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
    
    def test_complex_assignment(self):
        input = """
            a[a[i + 1] + f()] <- [1, 2, 3]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
        
        input = """
            a[f(f(f()))][1] <- [1] 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))

        input = """
            a[f(f(f()))][1][f() + a[3]] <- 10 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))

        input = """
            a[f(f(f()))][1][f() + a[3]] <- 10 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))

        input = """
            a[[3][1]] <- 10 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))

        input = """
            a[ord("Hello"[1])] <- 10 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))


        input = """
            a[1,f(),a[i]] <- 10 ## This is a comment
            b[1,2,3] <- 3 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))

    def test_programs(self):
        """Test programs"""
        input = """
            func areDivisors(number num1, number num2)
                return ((num1 % num2 = 0) or (num2 % num1 = 0))
            
            func main()
                begin
                    var num1 <- readNumber()
                    var num2 <- readNumber()
                    if (areDivisors(num1, num2)) writeString("Yes")
                    else writeString("No")
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))

        input = """
            func isPrime(number x)
            
            func main()
                begin
                    number x <- readNumber()
                        if (isPrime(x)) writeString("Yes")
                    else writeString("No")
                end
            
                func isPrime(number x)
                    begin
                        if (x <= 1) return false
                        var i <- 2
                        for i until i > x / 2 by 1
                            begin
                                if (x % i = 0) return false
                            end
                        return true
                    end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))
    
    def test_invalid_programs(self):
        """Test invalid programs"""
        input = """
            a[3][ <- 3
        """
        expect = "Error on line 2 col 18: <-"
        self.assertTrue(TestParser.test(input,expect,272))

        input = """
            number a[ <- [1]
        """
        expect = "Error on line 2 col 22: <-"
        self.assertTrue(TestParser.test(input,expect,273))
 
        input = """
            number [a] <- 3
        """
        expect = "Error on line 2 col 19: ["
        self.assertTrue(TestParser.test(input,expect,274))
 
        input = """
            dynamic [a] <- 3
        """
        expect = "Error on line 2 col 20: ["
        self.assertTrue(TestParser.test(input,expect,275))

        input = """
            var [a] <- 3
        """
        expect = "Error on line 2 col 16: ["
        self.assertTrue(TestParser.test(input,expect,276))

        input = """
            var [a]
        """
        expect = "Error on line 2 col 16: ["
        self.assertTrue(TestParser.test(input,expect,278))

        input = """
            for until 3 by 1
                do_something()
        """
        expect = "Error on line 2 col 16: until"
        self.assertTrue(TestParser.test(input,expect,279))

        input = """
            for until 3 by 1
                do_something()
        """
        expect = "Error on line 2 col 16: until"
        self.assertTrue(TestParser.test(input,expect,280))

        input = """
            for i until by 1
                do_something()
        """
        expect = "Error on line 2 col 24: by"
        self.assertTrue(TestParser.test(input,expect,281))

        input = """
            for i until 10 by
                do_something()
        """
        expect = "Error on line 2 col 29: \n"
        self.assertTrue(TestParser.test(input,expect,282))

        input = """
            for i until 10 by do_something()
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,283))
        
        input = """
            f(()
        """
        expect = "Error on line 2 col 15: )"
        self.assertTrue(TestParser.test(input,expect,284))

        input = """
            f(a[)
        """
        expect = "Error on line 2 col 16: )"
        self.assertTrue(TestParser.test(input,expect,285))

        input = """
            f[(])
        """
        expect = "Error on line 2 col 15: ]"
        self.assertTrue(TestParser.test(input,expect,286))

        input = """
            [[1,2,3,4],[1,2,3,5]][0 1] <- 3
        """
        expect = "Error on line 2 col 36: 1"
        self.assertTrue(TestParser.test(input,expect,287))

        input = """
            [[1 +, 2]][0,0] <- 3
        """
        expect = "Error on line 2 col 17: ,"
        self.assertTrue(TestParser.test(input,expect,288))

        input = """
            1, 2
        """
        expect = "Error on line 2 col 13: ,"
        self.assertTrue(TestParser.test(input,expect,289))
  
        input = """
            (1, 2)
        """
        expect = "Error on line 2 col 14: ,"
        self.assertTrue(TestParser.test(input,expect,290))

        input = """
            f(1 + , 2)
        """
        expect = "Error on line 2 col 18: ,"
        self.assertTrue(TestParser.test(input,expect,291))

        input = """
            func return 10
        """
        expect = "Error on line 2 col 17: return"
        self.assertTrue(TestParser.test(input,expect,292))

        input = """
            func begin() return 10 end
        """
        expect = "Error on line 2 col 17: begin"
        self.assertTrue(TestParser.test(input,expect,293))

        input = """
            func
            main()
            return 10
        """
        expect = "Error on line 2 col 16: \n"
        self.assertTrue(TestParser.test(input,expect,294))

        input = """
            func return return 10
        """
        expect = "Error on line 2 col 17: return"
        self.assertTrue(TestParser.test(input,expect,295))

    def test_newlines(self):
        """Test newlines""" 
        input = """
            func main()




            ## 121202








            return 10
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))


        input = """
            for i until 10 by 1 ## 123
            ##1212





            ### 1212
                do_something()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))

        input = """
            if (5) ### abc
            ## 12312
                3 ### 122
            ## 121212
            elif (5) ## 1212
            ###1 1212
                10
            ### else
            else ## 2
                3 ### 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))

        input = """
            begin
            ##1211

            ## 121212
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))