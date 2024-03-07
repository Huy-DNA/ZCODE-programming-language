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
        self.assertTrue(TestParser.test("var a <- 1 + 2 * 3", "successful",207))
        self.assertTrue(TestParser.test("var a <- 1 / 2 * 3", "successful",208))
        self.assertTrue(TestParser.test("var a <- 1 - 2 / 3", "successful",209))
        self.assertTrue(TestParser.test("var a <- 1 + 2 or 3", "successful",210))
        self.assertTrue(TestParser.test("var a <- (1 + 2) or (3 and 4)", "successful",211))
        self.assertTrue(TestParser.test("var a <- 1 + 2 ... 3 + 5", "successful",212))
        self.assertTrue(TestParser.test("var a <- a = b = c", "Error on line 1 col 15: =",213))
        self.assertTrue(TestParser.test("var a <- a % 2 = 0 or b % 2 = 0", "Error on line 1 col 28: =",214))
        self.assertTrue(TestParser.test("var a <- a = (b = c)", "successful",215))
        self.assertTrue(TestParser.test("var a <- a ... b ... c", "Error on line 1 col 17: ...",216))
        self.assertTrue(TestParser.test("var a <- (a ... b) ... c", "successful",217))
        self.assertTrue(TestParser.test("var a <- (a % 2 = 0) or (b % 2 = 0)", "successful",218))
        self.assertTrue(TestParser.test("var a <- a < b < c", "Error on line 1 col 15: <",219))
        self.assertTrue(TestParser.test("var a <- a > b > c", "Error on line 1 col 15: >",220))
        self.assertTrue(TestParser.test("var a <- a != b != c", "Error on line 1 col 16: !=",221))
        self.assertTrue(TestParser.test("var a <- a >= b >= c", "Error on line 1 col 16: >=",222))
        self.assertTrue(TestParser.test("var a <- a <= b <= c", "Error on line 1 col 16: <=",223))
        self.assertTrue(TestParser.test("var a <- a <= b >= c", "Error on line 1 col 16: >=",224))
        self.assertTrue(TestParser.test("var a <- a == b == c", "Error on line 1 col 16: ==",225))
        self.assertTrue(TestParser.test("var a <- a == b >= c", "Error on line 1 col 16: >=",226))
        self.assertTrue(TestParser.test("var a <- a <= b >= c", "Error on line 1 col 16: >=",227))
        self.assertTrue(TestParser.test("var a <- a = b <= c", "Error on line 1 col 15: <=",228))
        self.assertTrue(TestParser.test("var a <- a...b", "successful", 229))
    
    def test_if(self):
        """If statement"""
        input = """
        func main() begin
        if (3) 5 ## This is a comment
        if (4) 5
        if (5) if (6) 5
        if (1 + 2) if (3 + 4) if (5 + 6) "abcd"
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_elif(self):
        """If and elif statement"""
        input = """
        func main() begin
        if (3) 5 ## This is a comment
        elif (4) 5
        elif (5) 8 elif (6) 5
        if (1 + 2) if (3 + 4) if (5 + 6) 10 elif ("abcd") "aaaa" ... "bbbb"
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_invalid_if(self):
        """Invalid if statement"""
        input = """
        func main() begin
        if (3) ## This is a comment
        end
        """
        expect = "Error on line 4 col 8: end"
        self.assertTrue(TestParser.test(input,expect,232))

        input = """
        func main() begin
        if 3 ## This is a comment
        end
        """
        expect = "Error on line 3 col 11: 3"
        self.assertTrue(TestParser.test(input,expect,233))

        input = """
        func main() begin
        if ## This is a comment
        elif (10) 5
        end
        """
        expect = "Error on line 3 col 31: \n"
        self.assertTrue(TestParser.test(input,expect,234))
 
        input = """
        func main() begin
        if (3) ## This is a comment
        elif (10)
        end
        """
        expect = "Error on line 4 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,235))

        input = """
        func main() begin
        if (3) 5 ## This is a comment
        elif (10)
        end
        """
        expect = "Error on line 5 col 8: end"
        self.assertTrue(TestParser.test(input,expect,236))

        input = """
        func main() begin
        if (3) 5 ## This is a comment
        elif (10)
        elif (8) 3
        end
        """
        expect = "Error on line 5 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,237))

        input = """
        func main() begin
        if (3) ## This is a comment
        elif
        end
        """
        expect = "Error on line 4 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,238))

        input = """
        func main() begin
        if (3) ## This is a comment
        else
        end
        """
        expect = "Error on line 4 col 8: else"
        self.assertTrue(TestParser.test(input,expect,239))

        input = """
        func main() begin
        if (3) ## This is a comment
        elif (10)
        else
        end
        """
        expect = "Error on line 4 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,240))

        input = """
        func main() begin
        if (3) ## This is a comment
        elif
        else
        end
        """
        expect = "Error on line 4 col 8: elif"
        self.assertTrue(TestParser.test(input,expect,241))

        input = """
        func main() begin
        if
        elif
        else
        end
        """
        expect = "Error on line 3 col 10: \n"
        self.assertTrue(TestParser.test(input,expect,242))
    
    def test_else(self):
        """Test else"""
        input = """
        func main() begin 
        if (3) 10 ## This is a comment
        elif (5)
            if (6) 10
            elif (5) 10
            else 10
        else 10
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))

        input = """
        func main() begin 
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
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_decl(self):
        """Test declaration"""
        input = """
        func main() begin 
            number a_ <- 1
            bool b <- true
            string _c_d_ <- "abc'""
            number a[4] <- [1,2,3,4]
            bool b[5] <- [true, false, true, false, true]
            string C1c[1] <- ["123"]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

        input = """
        func main() begin 
            type a_ <- 1
        end
        """
        expect = "Error on line 3 col 17: a_"
        self.assertTrue(TestParser.test(input,expect,246))

        input = """
        func main() begin 
            number a_
            bool b
            string _c_d_
            number a[4,5,6]
            bool b[5,1]
            string C1c[1]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))

        input = """
        func main() begin 
            number a[4,[4]] <- [1,2,3,4]
        end
        """
        expect = "Error on line 3 col 23: ["
        self.assertTrue(TestParser.test(input,expect,248))
 
        input = """
        func main() begin 
            number a[4,"Hello"] <- [1,2,3,4]
        end
        """
        expect = "Error on line 3 col 23: Hello"
        self.assertTrue(TestParser.test(input,expect,249))

        input = """
        func main() begin 
            number a[4,1+2] <- [1,2,3,4]
        end
        """
        expect = "Error on line 3 col 24: +"
        self.assertTrue(TestParser.test(input,expect,250))

        input = """
        func main() begin 
            number a[] <- [1,2,3,4]
        end
        """
        expect = "Error on line 3 col 21: ]"
        self.assertTrue(TestParser.test(input,expect,251))

        input = """
        func main() begin 
            number a[1][1] <- [1,2,3,4]
        end
        """
        expect = "Error on line 3 col 23: ["
        self.assertTrue(TestParser.test(input,expect,252))

        input = """
        func main() begin 
            number a[] <- [1,2,3,4]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))

        input = """
        func main() begin 
            var a
            number b <- 3
        end
        """
        expect = "Error on line 3 col 17: \n"
        self.assertTrue(TestParser.test(input,expect,254))

        input = """
        func main() begin 
            var a <- 3
            var c <- "aaa'""
            var t <- true
            number b <- 3
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))

        input = """
        func main() begin 
            dynamic a <- 3
            dynamic c <- "aaa'""
            dynamic t <- true
            dynamic b
            b <- 3
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))

        input = """
            var a <- ### This a decl
            3
        """
        expect = "Error on line 2 col 36: \n"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_assignment(self):
        """Test assignment"""
        input = """
        func main() begin 
           a <- 3
           b <- "aaa" ... "bbb"
           c <- 1 + 2 + 3
           d <- 1 * 3 / 2 % true and false ... "abc" 
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))

        input = """
        func main() begin 
            a <- ## This is a comment
            1 + 2
        end
        """
        expect = "Error on line 3 col 37: \n"
        self.assertTrue(TestParser.test(input,expect,259))

    def test_for(self): 
        input = """
        func main() begin 
            for i until 10 by 1
            ## 1212

            ### 1221


                a <- a + 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))

        input = """
        func main() begin
            for i until x + 10 by 2 begin
                b <- a[i]
                a <- x + 10
                if (a[i] % 3 == 0)
                    break
            end 
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))

        input = """
        func main() begin
            for f until a[i] by 1 + 1
            ## 123
            ## 12212

            begin
                f()
                f()
                continue
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
    
    def test_complex_assignment(self):
        input = """
        func main() begin
            a[a[i + 1] + f()] <- [1, 2, 3]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
        
        input = """
        func main() begin
            a[f(f(f()))][1] <- [1] 
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))

        input = """
        func main() begin
            a[f(f(f()))][1][f() + a[3]] <- 10 
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))

        input = """
        func main() begin
            a[f(f(f()))][1][f() + a[3]] <- 10 
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))

        input = """
        func main() begin
            a[[3][1]] <- 10 
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))

        input = """
        func main() begin
            a[ord("Hello"[1])] <- 10 
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))


        input = """
        func main() begin
            a[1,f(),a[i]] <- 10 ## This is a comment
            b[1,2,3] <- 3 
        end
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
        func main() begin
            a[3][ <- 3
        end
        """
        expect = "Error on line 3 col 18: <-"
        self.assertTrue(TestParser.test(input,expect,272))

        input = """
        func main() begin
            number a[ <- [1]
        end
        """
        expect = "Error on line 3 col 22: <-"
        self.assertTrue(TestParser.test(input,expect,273))
 
        input = """
        func main() begin
            number [a] <- 3
        end
        """
        expect = "Error on line 3 col 19: ["
        self.assertTrue(TestParser.test(input,expect,274))
 
        input = """
        func main() begin
            dynamic [a] <- 3
        end
        """
        expect = "Error on line 3 col 20: ["
        self.assertTrue(TestParser.test(input,expect,275))

        input = """
        func main() begin
            var [a] <- 3
        end
        """
        expect = "Error on line 3 col 16: ["
        self.assertTrue(TestParser.test(input,expect,276))

        input = """
        func main() begin
            var [a]
        end
        """
        expect = "Error on line 3 col 16: ["
        self.assertTrue(TestParser.test(input,expect,278))

        input = """
        func main() begin
            for until 3 by 1
                do_something()
        end
        """
        expect = "Error on line 3 col 16: until"
        self.assertTrue(TestParser.test(input,expect,279))

        input = """
        func main() begin
            for until 3 by 1
                do_something()
        end
        """
        expect = "Error on line 3 col 16: until"
        self.assertTrue(TestParser.test(input,expect,280))

        input = """
        func main() begin
            for i until by 1
                do_something()
        end
        """
        expect = "Error on line 3 col 24: by"
        self.assertTrue(TestParser.test(input,expect,281))

        input = """
        func main() begin
            for i until 10 by
                do_something()
        end
        """
        expect = "Error on line 3 col 29: \n"
        self.assertTrue(TestParser.test(input,expect,282))

        input = """
        func main() begin
            for i until 10 by do_something()
        end
        """
        expect = "Error on line 4 col 8: end"
        self.assertTrue(TestParser.test(input,expect,283))
        
        input = """
        func main() begin
            f(()
        end
        """
        expect = "Error on line 3 col 15: )"
        self.assertTrue(TestParser.test(input,expect,284))

        input = """
        func main() begin
            f(a[)
        end
        """
        expect = "Error on line 3 col 16: )"
        self.assertTrue(TestParser.test(input,expect,285))

        input = """
        func main() begin
            f[(])
        end
        """
        expect = "Error on line 3 col 15: ]"
        self.assertTrue(TestParser.test(input,expect,286))

        input = """
        func main() begin
            [[1,2,3,4],[1,2,3,5]][0 1] <- 3
        end
        """
        expect = "Error on line 3 col 36: 1"
        self.assertTrue(TestParser.test(input,expect,287))

        input = """
        func main() begin
            [[1 +, 2]][0,0] <- 3
        end
        """
        expect = "Error on line 3 col 17: ,"
        self.assertTrue(TestParser.test(input,expect,288))

        input = """
        func main() begin
            1, 2
        end
        """
        expect = "Error on line 3 col 13: ,"
        self.assertTrue(TestParser.test(input,expect,289))
  
        input = """
        func main() begin
            (1, 2)
        end
        """
        expect = "Error on line 3 col 14: ,"
        self.assertTrue(TestParser.test(input,expect,290))

        input = """
        func main() begin
            f(1 + , 2)
        end
        """
        expect = "Error on line 3 col 18: ,"
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
        func main() begin
            for i until 10 by 1 ## 123
            ##1212





            ### 1212
                do_something()
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))

        input = """
        func main() begin
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
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))

        input = """
        func main()
            begin
            ##1211

            ## 121212
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))