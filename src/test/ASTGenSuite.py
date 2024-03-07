import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
    def test_301(self):
        input = '''
            func main() return 3
        '''
        expect = '''Program([FuncDecl(Id(main), [], Return(NumLit(3.0)))])'''
        self.assertTrue(TestAST.test(input, expect, 301))
    def test_302(self):
        input = '''
            func main()
        '''
        expect = '''Program([FuncDecl(Id(main), [], None)])'''
        self.assertTrue(TestAST.test(input, expect, 302))	
    def test_303(self):
        input = '''
            func main() begin

            end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([]))])'''
        self.assertTrue(TestAST.test(input, expect, 303))
    def test_304(self):
        input = '''
        func main() begin
            a <- 3
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), NumLit(3.0))]))])'''
        self.assertTrue(TestAST.test(input, expect, 304))
    def test_305(self):
        input = '''
        func main() begin
            var a <- 3
            dynamic b
            number c <- 3.0
            string d <- "acb"
            bool e <- true
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(3.0)), VarDecl(Id(b), None, dynamic, None), VarDecl(Id(c), NumberType, None, NumLit(3.0)), VarDecl(Id(d), StringType, None, StringLit(acb)), VarDecl(Id(e), BoolType, None, BooleanLit(True))]))])'''
        self.assertTrue(TestAST.test(input, expect, 305))
    def test_306(self):
        input = '''
        func main() begin
            for i until 10 by 1
                print(i)
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([For(Id(i), NumLit(10.0), NumLit(1.0), CallStmt(Id(print), [Id(i)]))]))])'''
        self.assertTrue(TestAST.test(input, expect, 306))
    def test_307(self):
        input = '''
        func main() begin
            if (i == 1)
                print(1)
            elif (i > 1)
                if (i == 2)
                    print(2)
                elif (i == 3)
                    print(3)
                else print("i > 3")
            else
                if (i == 0)
                    print(0)
                else print("i < 0")
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, Id(i), NumLit(1.0)), CallStmt(Id(print), [NumLit(1.0)])), [(BinaryOp(>, Id(i), NumLit(1.0)), If((BinaryOp(==, Id(i), NumLit(2.0)), CallStmt(Id(print), [NumLit(2.0)])), [(BinaryOp(==, Id(i), NumLit(3.0)), CallStmt(Id(print), [NumLit(3.0)]))], CallStmt(Id(print), [StringLit(i > 3)])))], If((BinaryOp(==, Id(i), NumLit(0.0)), CallStmt(Id(print), [NumLit(0.0)])), [], CallStmt(Id(print), [StringLit(i < 0)])))]))])'''
        self.assertTrue(TestAST.test(input, expect, 307))
    def test_308(self):
        input = '''
        func main() begin
            number a[3] <- [1, 2, 3]
            number b[1, 1] <- [[1]]
            string c[1, 2] <- [["aa", "bb"]]
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), VarDecl(Id(b), ArrayType([1.0, 1.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0)))), VarDecl(Id(c), ArrayType([1.0, 2.0], StringType), None, ArrayLit(ArrayLit(StringLit(aa), StringLit(bb))))]))])'''
        self.assertTrue(TestAST.test(input, expect, 308))
    def test_309(self):
        input = '''
            func gcd(number a, number b) begin
                if (a == b)
                    return a
                if (a < b)
                    return gcd(a, b - a)
                return gcd(a - b, b)
            end
        '''
        expect = '''Program([FuncDecl(Id(gcd), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(==, Id(a), Id(b)), Return(Id(a))), [], None), If((BinaryOp(<, Id(a), Id(b)), Return(CallExpr(Id(gcd), [Id(a), BinaryOp(-, Id(b), Id(a))]))), [], None), Return(CallExpr(Id(gcd), [BinaryOp(-, Id(a), Id(b)), Id(b)]))]))])'''
        self.assertTrue(TestAST.test(input, expect, 309))
    def test_310(self):
        input = '''
            func gcd(number a, number b)

            func gcd(number a, number b) begin
                if (a == b)
                    return a
                if (a < b)
                    return gcd(a, b - a)
                return gcd(a - b, b)
            end
        '''
        expect = '''Program([FuncDecl(Id(gcd), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], None), FuncDecl(Id(gcd), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(==, Id(a), Id(b)), Return(Id(a))), [], None), If((BinaryOp(<, Id(a), Id(b)), Return(CallExpr(Id(gcd), [Id(a), BinaryOp(-, Id(b), Id(a))]))), [], None), Return(CallExpr(Id(gcd), [BinaryOp(-, Id(a), Id(b)), Id(b)]))]))])'''
        self.assertTrue(TestAST.test(input, expect, 310))
    def test_311(self):
        input = '''
        func main() begin
            begin
            end
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([])]))])'''
        self.assertTrue(TestAST.test(input, expect, 311))
    def test_312(self):
        input = '''
        func main() begin
            var a <- [1, 1, 1, 1, 1, 2, 4]
            var i <- 0
            for i until len(a) - 1 by 1 begin
                if (i == 1)
                    continue
                print(i)
                if (i == 2)
                    break
            end
        end  
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, ArrayLit(NumLit(1.0), NumLit(1.0), NumLit(1.0), NumLit(1.0), NumLit(1.0), NumLit(2.0), NumLit(4.0))), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(-, CallExpr(Id(len), [Id(a)]), NumLit(1.0)), NumLit(1.0), Block([If((BinaryOp(==, Id(i), NumLit(1.0)), Continue), [], None), CallStmt(Id(print), [Id(i)]), If((BinaryOp(==, Id(i), NumLit(2.0)), Break), [], None)]))]))])'''
        self.assertTrue(TestAST.test(input, expect, 312))
    def test_313(self):
        input = '''
        ## This is a comment
        var a <- 3
        '''
        expect = '''Program([VarDecl(Id(a), None, var, NumLit(3.0))])'''
        self.assertTrue(TestAST.test(input, expect, 313))
    def test_314(self):
        input = '''
            var a1 <- false
            var a2 <- true
            var a3 <- (a1 and a2) or a1 and a3
        '''
        expect = '''Program([VarDecl(Id(a1), None, var, BooleanLit(False)), VarDecl(Id(a2), None, var, BooleanLit(True)), VarDecl(Id(a3), None, var, BinaryOp(and, BinaryOp(or, BinaryOp(and, Id(a1), Id(a2)), Id(a1)), Id(a3)))])'''
        self.assertTrue(TestAST.test(input, expect, 314))
    def test_315(self):
        input = '''
            string a <- "acbd"
            string b <- "acdb"
            string c <- a ... b
        '''
        expect = '''Program([VarDecl(Id(a), StringType, None, StringLit(acbd)), VarDecl(Id(b), StringType, None, StringLit(acdb)), VarDecl(Id(c), StringType, None, BinaryOp(..., Id(a), Id(b)))])'''
        self.assertTrue(TestAST.test(input, expect, 315))
    def test_316(self):
        input = '''
            number a <- 3
            number b <- 4
            number c <- a + b * b - c - a / a % a
        '''
        expect = '''Program([VarDecl(Id(a), NumberType, None, NumLit(3.0)), VarDecl(Id(b), NumberType, None, NumLit(4.0)), VarDecl(Id(c), NumberType, None, BinaryOp(-, BinaryOp(-, BinaryOp(+, Id(a), BinaryOp(*, Id(b), Id(b))), Id(c)), BinaryOp(%, BinaryOp(/, Id(a), Id(a)), Id(a))))])'''
        self.assertTrue(TestAST.test(input, expect, 316))
    def test_317(self):
        input = '''
            func ord(string a)

            func main() return ord("a")

            func ord(string a) begin
                return 3
            end
        '''
        expect = '''Program([FuncDecl(Id(ord), [VarDecl(Id(a), StringType, None, None)], None), FuncDecl(Id(main), [], Return(CallExpr(Id(ord), [StringLit(a)]))), FuncDecl(Id(ord), [VarDecl(Id(a), StringType, None, None)], Block([Return(NumLit(3.0))]))])'''
        self.assertTrue(TestAST.test(input, expect, 317))
    def test_318(self):
        input = '''
        
        func main() begin
            return
            break
            continue
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Return(), Break, Continue]))])'''
        self.assertTrue(TestAST.test(input, expect, 318))
    def test_319(self):
        input = '''
        func main() begin
            1
            "1"
            1e-10
            1E10
            [1, 2, 3]
            (1 + 2)
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([NumLit(1.0), StringLit(1), NumLit(1e-10), NumLit(10000000000.0), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), BinaryOp(+, NumLit(1.0), NumLit(2.0))]))])'''
        self.assertTrue(TestAST.test(input, expect, 319))
    def test_320(self):
        input = '''
        func main() begin
            a
            a1
            b2
            _a
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Id(a), Id(a1), Id(b2), Id(_a)]))])'''
        self.assertTrue(TestAST.test(input, expect, 320))
    def test_321(self):
        input = '''
        func main() begin
            var a <- int(input("prompt"))
            return a
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, CallExpr(Id(int), [CallExpr(Id(input), [StringLit(prompt)])])), Return(Id(a))]))])'''
        self.assertTrue(TestAST.test(input, expect, 321))
    def test_322(self):
        input = '''
            func plusOne(number arr[10]) begin
                var i <- 0
                for i until 9 by 1
                    arr[0] = arr[0] + 1
            end
        '''
        expect = '''Program([FuncDecl(Id(plusOne), [VarDecl(Id(arr), ArrayType([10.0], NumberType), None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), NumLit(9.0), NumLit(1.0), BinaryOp(=, ArrayCell(Id(arr), [NumLit(0.0)]), BinaryOp(+, ArrayCell(Id(arr), [NumLit(0.0)]), NumLit(1.0))))]))])'''
        self.assertTrue(TestAST.test(input, expect, 322))
    def test_323(self):
        input = '''
        func main() begin
            a[f()] <- g()
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [CallExpr(Id(f), [])]), CallExpr(Id(g), []))]))])'''
        self.assertTrue(TestAST.test(input, expect, 323))
    def test_324(self):
        input = '''
        func main() begin
            f()[1, 2] <- [[1, 2]]
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(CallExpr(Id(f), []), [NumLit(1.0), NumLit(2.0)]), ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))]))])'''
        self.assertTrue(TestAST.test(input, expect, 324))
    def test_325(self):
        input = '''
        func main() begin
            1[2]() <- 2()
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(CallExpr(ArrayCell(NumLit(1.0), [NumLit(2.0)]), []), CallExpr(NumLit(2.0), []))]))])'''
        self.assertTrue(TestAST.test(input, expect, 325))
    def test_326(self):
        input = '''
        func main() begin
            2()()()[1][1] <- 3
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(ArrayCell(CallExpr(CallExpr(CallExpr(NumLit(2.0), []), []), []), [NumLit(1.0)]), [NumLit(1.0)]), NumLit(3.0))]))])'''
        self.assertTrue(TestAST.test(input, expect, 326))
    def test_327(self):
        input = '''
        func main() begin
            10 * 10 = 1 ... 1
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([BinaryOp(..., BinaryOp(=, BinaryOp(*, NumLit(10.0), NumLit(10.0)), NumLit(1.0)), NumLit(1.0))]))])'''
        self.assertTrue(TestAST.test(input, expect, 327))
    def test_328(self):
        input = '''
        func main() begin
            1 + 2 == 2 ... 3 - 3 * 4 = 10() + (3 + 2)
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([BinaryOp(..., BinaryOp(==, BinaryOp(+, NumLit(1.0), NumLit(2.0)), NumLit(2.0)), BinaryOp(=, BinaryOp(-, NumLit(3.0), BinaryOp(*, NumLit(3.0), NumLit(4.0))), BinaryOp(+, CallExpr(NumLit(10.0), []), BinaryOp(+, NumLit(3.0), NumLit(2.0)))))]))])'''
        self.assertTrue(TestAST.test(input, expect, 328))
    def test_329(self):
        input = '''
            func t(bool flag, number i) begin
                if (flag)
                    return i
                return 0
            end
        '''
        expect = '''Program([FuncDecl(Id(t), [VarDecl(Id(flag), BoolType, None, None), VarDecl(Id(i), NumberType, None, None)], Block([If((Id(flag), Return(Id(i))), [], None), Return(NumLit(0.0))]))])'''
        self.assertTrue(TestAST.test(input, expect, 329))
    def test_330(self):
        input = '''
            func countToN(number n) begin
                print(n)
                if (n > 0)
                    countToN(n - 1) 
            end
        '''
        expect = '''Program([FuncDecl(Id(countToN), [VarDecl(Id(n), NumberType, None, None)], Block([CallStmt(Id(print), [Id(n)]), If((BinaryOp(>, Id(n), NumLit(0.0)), CallStmt(Id(countToN), [BinaryOp(-, Id(n), NumLit(1.0))])), [], None)]))])'''
        self.assertTrue(TestAST.test(input, expect, 330))
    def test_331(self):
        input = '''
            func main() return a
        '''
        expect = '''Program([FuncDecl(Id(main), [], Return(Id(a)))])'''
        self.assertTrue(TestAST.test(input, expect, 331))
    def test_332(self):
        input = '''
            func bar(number n) begin
                func foo() return n + 3
                return foo(10)
            end
        '''
        expect = '''Program([FuncDecl(Id(bar), [VarDecl(Id(n), NumberType, None, None)], Block([FuncDecl(Id(foo), [], Return(BinaryOp(+, Id(n), NumLit(3.0)))), Return(CallExpr(Id(foo), [NumLit(10.0)]))]))])'''
        self.assertTrue(TestAST.test(input, expect, 332))
    def test_333(self):
        input = '''
            func main() return main()
        '''
        expect = '''Program([FuncDecl(Id(main), [], Return(CallExpr(Id(main), [])))])'''
        self.assertTrue(TestAST.test(input, expect, 333))
    def test_334(self):
        input = '''
            dynamic a <- 1
        '''
        expect = '''Program([VarDecl(Id(a), None, dynamic, NumLit(1.0))])'''
        self.assertTrue(TestAST.test(input, expect, 334))
    def test_335(self):
        input = '''
            func read()

            func main() begin
                a <- read()
                print(a)
            end
        '''
        expect = '''Program([FuncDecl(Id(read), [], None), FuncDecl(Id(main), [], Block([AssignStmt(Id(a), CallExpr(Id(read), [])), CallStmt(Id(print), [Id(a)])]))])'''
        self.assertTrue(TestAST.test(input, expect, 335))
    def test_336(self):
        input = '''
            func main() begin
                main()
            end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([CallStmt(Id(main), [])]))])'''
        self.assertTrue(TestAST.test(input, expect, 336))
    def test_337(self):
        input = '''
            func foo(bool flag) begin
                if (flag)
                    func foo1() return 1
                else func foo1() return 2
                foo1()
            end
        '''
        expect = '''Program([FuncDecl(Id(foo), [VarDecl(Id(flag), BoolType, None, None)], Block([If((Id(flag), FuncDecl(Id(foo1), [], Return(NumLit(1.0)))), [], FuncDecl(Id(foo1), [], Return(NumLit(2.0)))), CallStmt(Id(foo1), [])]))])'''
        self.assertTrue(TestAST.test(input, expect, 337))
    def test_338(self):
        input = '''
            func concat(string a[10]) begin
                var i <- 0
                var res <- ""
                for i until 9 by 1
                    res <- res ... a[i]
                return res
            end
        '''
        expect = '''Program([FuncDecl(Id(concat), [VarDecl(Id(a), ArrayType([10.0], StringType), None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(res), None, var, StringLit()), For(Id(i), NumLit(9.0), NumLit(1.0), AssignStmt(Id(res), BinaryOp(..., Id(res), ArrayCell(Id(a), [Id(i)])))), Return(Id(res))]))])'''
        self.assertTrue(TestAST.test(input, expect, 338))
    def test_339(self):
        input = '''
            func sum(number a[10]) begin
                var i <- 0
                var res <- 0
                for i until 9 by 1
                    res <- res + a[i]
                return res
            end
        '''
        expect = '''Program([FuncDecl(Id(sum), [VarDecl(Id(a), ArrayType([10.0], NumberType), None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(res), None, var, NumLit(0.0)), For(Id(i), NumLit(9.0), NumLit(1.0), AssignStmt(Id(res), BinaryOp(+, Id(res), ArrayCell(Id(a), [Id(i)])))), Return(Id(res))]))])'''
        self.assertTrue(TestAST.test(input, expect, 339))
    def test_340(self):
        input = '''
        func main() begin
            a[1()] <- 1()		
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [CallExpr(NumLit(1.0), [])]), CallExpr(NumLit(1.0), []))]))])'''
        self.assertTrue(TestAST.test(input, expect, 340))
    def test_341(self):
        input = '''
        func main() begin
            b[f + 1()] <- c[1]
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(b), [BinaryOp(+, Id(f), CallExpr(NumLit(1.0), []))]), ArrayCell(Id(c), [NumLit(1.0)]))]))])'''
        self.assertTrue(TestAST.test(input, expect, 341))
    def test_342(self):
        input = '''
        func main() begin
            1 + 2[3]...3 <- 12
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(BinaryOp(..., BinaryOp(+, NumLit(1.0), ArrayCell(NumLit(2.0), [NumLit(3.0)])), NumLit(3.0)), NumLit(12.0))]))])'''
        self.assertTrue(TestAST.test(input, expect, 342))
    def test_343(self):
        input = '''
        func main() begin
            1 == 2 ... 10 <- "string" 
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(BinaryOp(..., BinaryOp(==, NumLit(1.0), NumLit(2.0)), NumLit(10.0)), StringLit(string))]))])'''
        self.assertTrue(TestAST.test(input, expect, 343))
    def test_344(self):
        input = '''
        func main() begin
            "string" <- 10
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(StringLit(string), NumLit(10.0))]))])'''
        self.assertTrue(TestAST.test(input, expect, 344))
    def test_345(self):
        input = '''
        func main() begin
            [1,2,3][0] <- 3
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), [NumLit(0.0)]), NumLit(3.0))]))])'''
        self.assertTrue(TestAST.test(input, expect, 345))
    def test_346(self):
        input = '''
        func main() begin
            [1,2][0] <- 0
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(ArrayLit(NumLit(1.0), NumLit(2.0)), [NumLit(0.0)]), NumLit(0.0))]))])'''
        self.assertTrue(TestAST.test(input, expect, 346))
    def test_347(self):
        input = '''
        func main() begin
            [[1,2], [2,3]][0] <- [2, 3]
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(2.0), NumLit(3.0))), [NumLit(0.0)]), ArrayLit(NumLit(2.0), NumLit(3.0)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 347))
    def test_348(self):
        input = '''
        func main() begin
            "string"[0] <- " "
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(StringLit(string), [NumLit(0.0)]), StringLit( ))]))])'''
        self.assertTrue(TestAST.test(input, expect, 348))
    def test_349(self):
        input = '''
        func main() begin
            ("ab"..."cd")[0] <- "c"
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(BinaryOp(..., StringLit(ab), StringLit(cd)), [NumLit(0.0)]), StringLit(c))]))])'''
        self.assertTrue(TestAST.test(input, expect, 349))
    def test_350(self):
        input = '''
        func main() begin
            x <- 10 + 20 * 3    
        end
        '''
        expect = '''Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(x), BinaryOp(+, NumLit(10.0), BinaryOp(*, NumLit(20.0), NumLit(3.0))))]))])'''
        self.assertTrue(TestAST.test(input, expect, 350))
    def test_351(self):
        input = '''
                func max_of_array(number arr[100]) begin
                    var max <- arr[0]    
                    i <- 0
                    for i until 99 by 1 begin
                        if (arr[i] > max)     
                            max <- arr[i]    
                    end
                    return max    
                end
            '''
        expect = '''Program([FuncDecl(Id(max_of_array), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None)], Block([VarDecl(Id(max), None, var, ArrayCell(Id(arr), [NumLit(0.0)])), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), NumLit(99.0), NumLit(1.0), Block([If((BinaryOp(>, ArrayCell(Id(arr), [Id(i)]), Id(max)), AssignStmt(Id(max), ArrayCell(Id(arr), [Id(i)]))), [], None)])), Return(Id(max))]))])'''
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_352(self):
        input = '''
            func sum_of_array(number arr[100]) begin
                var sum <- 0    
                var i <- 0
                for i until 99 by 1 begin
                    sum <- sum + arr[i]    
                end
                return sum    
            end
            '''
        expect = '''Program([FuncDecl(Id(sum_of_array), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None)], Block([VarDecl(Id(sum), None, var, NumLit(0.0)), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), NumLit(99.0), NumLit(1.0), Block([AssignStmt(Id(sum), BinaryOp(+, Id(sum), ArrayCell(Id(arr), [Id(i)])))])), Return(Id(sum))]))])'''
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_353(self):
        input = '''
            func product_of_array(number arr[10]) begin
                var product <- 1    
                var i <- 0
                for i until 10 - 1 by 1 begin
                    product <- product * arr[i]    
                end
                return product    
            end
            '''
        expect = '''Program([FuncDecl(Id(product_of_array), [VarDecl(Id(arr), ArrayType([10.0], NumberType), None, None)], Block([VarDecl(Id(product), None, var, NumLit(1.0)), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(-, NumLit(10.0), NumLit(1.0)), NumLit(1.0), Block([AssignStmt(Id(product), BinaryOp(*, Id(product), ArrayCell(Id(arr), [Id(i)])))])), Return(Id(product))]))])'''
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_354(self):
        input = '''
            func is_positive(number n) begin
                if (n > 0)     
                    return true    
                else
                    return false    
            end
            '''
        expect = '''Program([FuncDecl(Id(is_positive), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(>, Id(n), NumLit(0.0)), Return(BooleanLit(True))), [], Return(BooleanLit(False)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_355(self):
        input = '''
            func is_negative(number n) begin
                if (n < 0)
                    return true    
                else
                    return false    
            end
            '''
        expect = '''Program([FuncDecl(Id(is_negative), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(<, Id(n), NumLit(0.0)), Return(BooleanLit(True))), [], Return(BooleanLit(False)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_356(self):
        input = '''
            func is_13(number n) begin
                if (n == 13)     
                    return true    
                else
                    return false    
            end
            '''
        expect = '''Program([FuncDecl(Id(is_13), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(==, Id(n), NumLit(13.0)), Return(BooleanLit(True))), [], Return(BooleanLit(False)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_357(self):
        input = '''
            func negate_absolute_value(number n) begin
                if (n < 0)     
                    return n    
                else
                    return -n    
            end
            '''
        expect = '''Program([FuncDecl(Id(negate_absolute_value), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(<, Id(n), NumLit(0.0)), Return(Id(n))), [], Return(UnaryOp(-, Id(n))))]))])'''
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_358(self):
        input = '''
            func negate(number n) begin
                return -n    
            end
            '''
        expect = '''Program([FuncDecl(Id(negate), [VarDecl(Id(n), NumberType, None, None)], Block([Return(UnaryOp(-, Id(n)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_359(self):
        input = '''
        func main() begin
            begin
                var x <- 10
                return x
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(x), None, var, NumLit(10.0)), Return(Id(x))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_360(self):
        input = '''
            func sum(number a, number b) begin
                return a + b    
            end
            '''
        expect = '''Program([FuncDecl(Id(sum), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(BinaryOp(+, Id(a), Id(b)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_361(self):
        input = '''
            func factorial(number n) begin
                if (n == 0)     
                    return 1    
                else
                    return n * factorial(n - 1)    
                end
            end
            '''
        expect = '''Program([FuncDecl(Id(factorial), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(==, Id(n), NumLit(0.0)), Return(NumLit(1.0))), [], Return(BinaryOp(*, Id(n), CallExpr(Id(factorial), [BinaryOp(-, Id(n), NumLit(1.0))]))))]))])'''
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_362(self):
        input = '''
        var a <- 3
        func main()
        func main() begin
            begin
                var i <- 0
                for i until 10 by 1 begin
                    if (i % 2 == 0)     
                        continue    
                    else
                        break    
                    end
                end
            end
        end
            '''
        expect = '''Program([VarDecl(Id(a), None, var, NumLit(3.0)), FuncDecl(Id(main), [], None), FuncDecl(Id(main), [], Block([Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), NumLit(10.0), NumLit(1.0), Block([If((BinaryOp(==, BinaryOp(%, Id(i), NumLit(2.0)), NumLit(0.0)), Continue), [], Break)]))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 362))
    def test_363(self):
        input = '''
            func power(number base, number exp) begin
                var result <- 1    
                var i <- 1
                for i until exp by 1 begin
                    result <- result * base    
                end
                return result    
            end
            '''
        expect = '''Program([FuncDecl(Id(power), [VarDecl(Id(base), NumberType, None, None), VarDecl(Id(exp), NumberType, None, None)], Block([VarDecl(Id(result), None, var, NumLit(1.0)), VarDecl(Id(i), None, var, NumLit(1.0)), For(Id(i), Id(exp), NumLit(1.0), Block([AssignStmt(Id(result), BinaryOp(*, Id(result), Id(base)))])), Return(Id(result))]))])'''
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_364(self):
        input = '''
            func fac(number n) begin
                if (n <= 0)     
                    return 1    
                else
                    return n * fac(n - 1)    
                end
            end
            '''
        expect = '''Program([FuncDecl(Id(fac), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(<=, Id(n), NumLit(0.0)), Return(NumLit(1.0))), [], Return(BinaryOp(*, Id(n), CallExpr(Id(fac), [BinaryOp(-, Id(n), NumLit(1.0))]))))]))])'''
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_365(self):
        input = '''
            func is_prime(number n) begin
                if (n <= 1)     
                    return false    
                i <- 2
                for i until sqrt(n) by 1 begin
                    if (n % i == 0)     
                        return false    
                end
                return true    
            end
            '''
        expect = '''Program([FuncDecl(Id(is_prime), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(<=, Id(n), NumLit(1.0)), Return(BooleanLit(False))), [], None), AssignStmt(Id(i), NumLit(2.0)), For(Id(i), CallExpr(Id(sqrt), [Id(n)]), NumLit(1.0), Block([If((BinaryOp(==, BinaryOp(%, Id(n), Id(i)), NumLit(0.0)), Return(BooleanLit(False))), [], None)])), Return(BooleanLit(True))]))])'''
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_366(self):
        input = '''
            func gcd(number a, number b) begin
                if (b != 0) begin
                    var temp <- b    
                    b <- a % b    
                    a <- temp    
                end
                return gcd(b, a)  
            end
            '''
        expect = '''Program([FuncDecl(Id(gcd), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(!=, Id(b), NumLit(0.0)), Block([VarDecl(Id(temp), None, var, Id(b)), AssignStmt(Id(b), BinaryOp(%, Id(a), Id(b))), AssignStmt(Id(a), Id(temp))])), [], None), Return(CallExpr(Id(gcd), [Id(b), Id(a)]))]))])'''
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_367(self):
        input = '''
            func lcm(number a, number b) begin
                return (a * b) / gcd(a, b)    
            end
            '''
        expect = '''Program([FuncDecl(Id(lcm), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(BinaryOp(/, BinaryOp(*, Id(a), Id(b)), CallExpr(Id(gcd), [Id(a), Id(b)])))]))])'''
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_368(self):
        input = '''
            func fibonacci(number n) begin
                if (n <= 1)     
                    return n    
                return fibonacci(n - 1) + fibonacci(n - 2)    
            end
            '''
        expect = '''Program([FuncDecl(Id(fibonacci), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(<=, Id(n), NumLit(1.0)), Return(Id(n))), [], None), Return(BinaryOp(+, CallExpr(Id(fibonacci), [BinaryOp(-, Id(n), NumLit(1.0))]), CallExpr(Id(fibonacci), [BinaryOp(-, Id(n), NumLit(2.0))])))]))])'''
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_369(self):
        input = '''
            func is_even(number n) begin
                if (n % 2 == 0)     
                    return true    
                else
                    return false    
                end
            end
            '''
        expect = '''Program([FuncDecl(Id(is_even), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(==, BinaryOp(%, Id(n), NumLit(2.0)), NumLit(0.0)), Return(BooleanLit(True))), [], Return(BooleanLit(False)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_370(self):
        input = '''
            func is_odd(number n) begin
                if (n % 2 == 0)     
                    return false    
                else
                    return true    
                end
            end
            '''
        expect = '''Program([FuncDecl(Id(is_odd), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(==, BinaryOp(%, Id(n), NumLit(2.0)), NumLit(0.0)), Return(BooleanLit(False))), [], Return(BooleanLit(True)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_371(self):
        input = '''
            func absolute_value(number n) begin
                if (n < 0)     
                    return -n    
                else
                    return n    
                end
            end
            '''
        expect = '''Program([FuncDecl(Id(absolute_value), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(<, Id(n), NumLit(0.0)), Return(UnaryOp(-, Id(n)))), [], Return(Id(n)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_372(self):
        input = '''
            func max(number a, number b) begin
                if (a > b)     
                    return a    
                else
                    return b    
                end
            end
            '''
        expect = '''Program([FuncDecl(Id(max), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(>, Id(a), Id(b)), Return(Id(a))), [], Return(Id(b)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_373(self):
        input = '''
        func main() begin
            begin
                var i <- 0 
                for i until 10 by 1 begin
                    if (i % 2 == 0)     
                        continue    
                    else
                        break    
                    end
                end
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), NumLit(10.0), NumLit(1.0), Block([If((BinaryOp(==, BinaryOp(%, Id(i), NumLit(2.0)), NumLit(0.0)), Continue), [], Break)]))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_374(self):
        input = '''
        func main() begin
            begin
                var i <- 1
                for i until 100000 by 3 begin
                    if (i % 5 == 0)     
                        continue    
                    else
                        break    
                    end
                end
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(i), None, var, NumLit(1.0)), For(Id(i), NumLit(100000.0), NumLit(3.0), Block([If((BinaryOp(==, BinaryOp(%, Id(i), NumLit(5.0)), NumLit(0.0)), Continue), [], Break)]))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_375(self):
        input = '''
        func main() begin
            begin
                var i <- 3   
                for i until -100 by -1 begin
                    if (i % -50 == 0)     
                        continue    
                    else
                        break    
                    end
                end
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(i), None, var, NumLit(3.0)), For(Id(i), UnaryOp(-, NumLit(100.0)), UnaryOp(-, NumLit(1.0)), Block([If((BinaryOp(==, BinaryOp(%, Id(i), UnaryOp(-, NumLit(50.0))), NumLit(0.0)), Continue), [], Break)]))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_376(self):
        input = '''
        func main() begin
            begin
                var i <- 100
                for i until 10 * 2 by 1 begin
                    if (i == 0)     
                        continue    
                    else
                        break    
                    end
                end
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(i), None, var, NumLit(100.0)), For(Id(i), BinaryOp(*, NumLit(10.0), NumLit(2.0)), NumLit(1.0), Block([If((BinaryOp(==, Id(i), NumLit(0.0)), Continue), [], Break)]))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_377(self):
        input = '''
        func main() begin
            begin
                var i <- 0
                for i until f() by 1 begin
                    if (i % 2 == 0)     
                        continue    
                    else
                        break    
                    end
                end
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), CallExpr(Id(f), []), NumLit(1.0), Block([If((BinaryOp(==, BinaryOp(%, Id(i), NumLit(2.0)), NumLit(0.0)), Continue), [], Break)]))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_378(self):
        input = '''
        func main() begin
            begin
                var i <- g()
                for i until a[2] by a[1] begin
                    if (a[i] % 2 == 0)     
                        continue    
                    else
                        break    
                    end
                end
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(i), None, var, CallExpr(Id(g), [])), For(Id(i), ArrayCell(Id(a), [NumLit(2.0)]), ArrayCell(Id(a), [NumLit(1.0)]), Block([If((BinaryOp(==, BinaryOp(%, ArrayCell(Id(a), [Id(i)]), NumLit(2.0)), NumLit(0.0)), Continue), [], Break)]))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_379(self):
        input = '''
        func main() begin
            begin
                var j <- 0
                for j until 100 by 1 begin
                    if (i % 3 == 0)     
                        continue    
                    else
                        break    
                    end
                end
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(j), None, var, NumLit(0.0)), For(Id(j), NumLit(100.0), NumLit(1.0), Block([If((BinaryOp(==, BinaryOp(%, Id(i), NumLit(3.0)), NumLit(0.0)), Continue), [], Break)]))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_380(self):
        input = '''
        func main() begin
            begin
                var x <- 10    
                return x    
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(x), None, var, NumLit(10.0)), Return(Id(x))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_381(self):
        input = '''
            func minus(number a, number b) begin
                return a - b    
            end
            '''
        expect = '''Program([FuncDecl(Id(minus), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(BinaryOp(-, Id(a), Id(b)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_382(self):
        input = '''
            func mul(number n, number b) begin
                return n * b
            end
            '''
        expect = '''Program([FuncDecl(Id(mul), [VarDecl(Id(n), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(BinaryOp(*, Id(n), Id(b)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_383(self):
        input = '''
            func is_not_zero(number n) begin
                return n != 0
            end
            '''
        expect = '''Program([FuncDecl(Id(is_not_zero), [VarDecl(Id(n), NumberType, None, None)], Block([Return(BinaryOp(!=, Id(n), NumLit(0.0)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_384(self):
        input = '''
        func main() begin
            begin
                var i <- 0
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(i), None, var, NumLit(0.0))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_385(self):
        input = '''
            func mod(number a, number b) begin
                return a % b    
            end
            '''
        expect = '''Program([FuncDecl(Id(mod), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(BinaryOp(%, Id(a), Id(b)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_386(self):
        input = '''
        func main() begin
            begin
                var i <- -10 
                for i until -10 by 100 begin
                    if (i % 2871 == 0)     
                        break
                end
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(i), None, var, UnaryOp(-, NumLit(10.0))), For(Id(i), UnaryOp(-, NumLit(10.0)), NumLit(100.0), Block([If((BinaryOp(==, BinaryOp(%, Id(i), NumLit(2871.0)), NumLit(0.0)), Break), [], None)]))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_387(self):
        input =  '''
            func inverse(number n) begin
               return 1 / n    
           end
		'''
        expect = '''Program([FuncDecl(Id(inverse), [VarDecl(Id(n), NumberType, None, None)], Block([Return(BinaryOp(/, NumLit(1.0), Id(n)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_388(self):
        input = '''
        func main() begin
            begin
                var arr <- [1, 2, 3, 4, 5]    
                i <- 0
                for i until len(arr) - 1 by 1 begin
                    arr[i] <- arr[i] * 2    
                end
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(arr), None, var, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0))), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(-, CallExpr(Id(len), [Id(arr)]), NumLit(1.0)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(arr), [Id(i)]), BinaryOp(*, ArrayCell(Id(arr), [Id(i)]), NumLit(2.0)))]))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_389(self):
        input = '''
            func max(number a, number b, number c) begin
                if ((a > b) and (a > c))     
                    return a    
                elif (b > c)
                    return b    
                return c
            end
            '''
        expect = '''Program([FuncDecl(Id(max), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None), VarDecl(Id(c), NumberType, None, None)], Block([If((BinaryOp(and, BinaryOp(>, Id(a), Id(b)), BinaryOp(>, Id(a), Id(c))), Return(Id(a))), [(BinaryOp(>, Id(b), Id(c)), Return(Id(b)))], None), Return(Id(c))]))])'''
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_390(self):
        input = '''
            func min(number a, number b) begin
                if (a < b)     
                    return a    
                else
                    return b    
            end
            '''
        expect = '''Program([FuncDecl(Id(min), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(<, Id(a), Id(b)), Return(Id(a))), [], Return(Id(b)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_391(self):
        input = '''
        func main() begin
            begin
                var arr <- [1, 2, 3, 4, 5]    
                i <- 0
                for i until len(arr) - 1 by 1 begin
                    sum <- sum + arr[i]    
                end
                return sum    
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(arr), None, var, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0))), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(-, CallExpr(Id(len), [Id(arr)]), NumLit(1.0)), NumLit(1.0), Block([AssignStmt(Id(sum), BinaryOp(+, Id(sum), ArrayCell(Id(arr), [Id(i)])))])), Return(Id(sum))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_392(self):
        input = '''
            func power_2(number exp) begin
                var result <- 1    
                var i <- 1
                for i until exp by 1 begin
                    result <- result * 2    
                end
                return result    
            end
            '''
        expect = '''Program([FuncDecl(Id(power_2), [VarDecl(Id(exp), NumberType, None, None)], Block([VarDecl(Id(result), None, var, NumLit(1.0)), VarDecl(Id(i), None, var, NumLit(1.0)), For(Id(i), Id(exp), NumLit(1.0), Block([AssignStmt(Id(result), BinaryOp(*, Id(result), NumLit(2.0)))])), Return(Id(result))]))])'''
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_393(self):
        input = '''
        func main() begin
            begin
                return 100 + "abc"
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([Return(BinaryOp(+, NumLit(100.0), StringLit(abc)))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_394(self):
        input = '''
        func main() begin
            begin
                var arr <- [1, 2, 3, 4, 5]    
                var product <- 1    
                i <- 0
                for i until len(arr) - 1 by 1 begin
                    product <- product * arr[i]    
                end
                return product    
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(arr), None, var, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0))), VarDecl(Id(product), None, var, NumLit(1.0)), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(-, CallExpr(Id(len), [Id(arr)]), NumLit(1.0)), NumLit(1.0), Block([AssignStmt(Id(product), BinaryOp(*, Id(product), ArrayCell(Id(arr), [Id(i)])))])), Return(Id(product))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_395(self):
        input = '''
        func main() begin
            begin
                var arr <- [1, 2, 3, 4, 5]    
                var max <- arr[0]    
                i <- 0
                for i until len(arr) - 1 by 1 begin
                    if (arr[i] > max)     
                        max <- arr[i]    
                end
                return max    
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(arr), None, var, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0))), VarDecl(Id(max), None, var, ArrayCell(Id(arr), [NumLit(0.0)])), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(-, CallExpr(Id(len), [Id(arr)]), NumLit(1.0)), NumLit(1.0), Block([If((BinaryOp(>, ArrayCell(Id(arr), [Id(i)]), Id(max)), AssignStmt(Id(max), ArrayCell(Id(arr), [Id(i)]))), [], None)])), Return(Id(max))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_396(self):
        input = '''
        func main() begin
            begin
                var arr <- [1, 2, 3, 4, 5]    
                var min <- arr[0]    
                i <- 0
                for i until len(arr) - 1 by 1 begin
                    if (arr[i] < min)     
                        min <- arr[i]    
                end
                return min    
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(arr), None, var, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0))), VarDecl(Id(min), None, var, ArrayCell(Id(arr), [NumLit(0.0)])), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(-, CallExpr(Id(len), [Id(arr)]), NumLit(1.0)), NumLit(1.0), Block([If((BinaryOp(<, ArrayCell(Id(arr), [Id(i)]), Id(min)), AssignStmt(Id(min), ArrayCell(Id(arr), [Id(i)]))), [], None)])), Return(Id(min))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_397(self):
        input = '''
        func main() begin
            begin
                var x <- 5    
                var y <- 10    
                if (x > y)     
                    return x    
                else
                    return y    
            end
        end
            '''
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(x), None, var, NumLit(5.0)), VarDecl(Id(y), None, var, NumLit(10.0)), If((BinaryOp(>, Id(x), Id(y)), Return(Id(x))), [], Return(Id(y)))])]))])'''
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_398(self):
        input = '''
            func is_zero(number n) begin
                if (n == 0)     
                    return true    
                else
                    return false    
                end
            end
            '''
        expect = '''Program([FuncDecl(Id(is_zero), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(==, Id(n), NumLit(0.0)), Return(BooleanLit(True))), [], Return(BooleanLit(False)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_399(self):
        input = '''
            func is_one(number n) begin
                return n == 1  
            end
            '''
        expect = '''Program([FuncDecl(Id(is_one), [VarDecl(Id(n), NumberType, None, None)], Block([Return(BinaryOp(==, Id(n), NumLit(1.0)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 399))
    def test_400(self):
        input = '''
            func is_two(number n) begin
                if (n == 2)     
                    return false    
                else
                    return true
            end
            '''
        expect = '''Program([FuncDecl(Id(is_two), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(==, Id(n), NumLit(2.0)), Return(BooleanLit(False))), [], Return(BooleanLit(True)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 400))