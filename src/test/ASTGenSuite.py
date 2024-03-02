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
			a <- 3
		'''
		expect = '''Program([AssignStmt(Id(a), NumLit(3.0))])'''
		self.assertTrue(TestAST.test(input, expect, 304))
	def test_305(self):
		input = '''
			var a <- 3
			dynamic b
			number c <- 3.0
			string d <- "acb"
			bool e <- true
		'''
		expect = '''Program([VarDecl(Id(a), None, var, NumLit(3.0)), VarDecl(Id(b), None, dynamic, None), VarDecl(Id(c), NumberType, None, NumLit(3.0)), VarDecl(Id(d), StringType, None, StringLit(acb)), VarDecl(Id(e), BoolType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 305))
	def test_306(self):
		input = '''
			for i until 10 by 1
				print(i)
		'''
		expect = '''Program([For(Id(i), NumLit(10.0), NumLit(1.0), CallStmt(Id(print), [Id(i)]))])'''
		self.assertTrue(TestAST.test(input, expect, 306))
	def test_307(self):
		input = '''
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
		'''
		expect = '''Program([If((BinaryOp(==, Id(i), NumLit(1.0)), CallStmt(Id(print), [NumLit(1.0)])), [(BinaryOp(>, Id(i), NumLit(1.0)), If((BinaryOp(==, Id(i), NumLit(2.0)), CallStmt(Id(print), [NumLit(2.0)])), [(BinaryOp(==, Id(i), NumLit(3.0)), CallStmt(Id(print), [NumLit(3.0)]))], CallStmt(Id(print), [StringLit(i > 3)])))], If((BinaryOp(==, Id(i), NumLit(0.0)), CallStmt(Id(print), [NumLit(0.0)])), [], CallStmt(Id(print), [StringLit(i < 0)])))])'''
		self.assertTrue(TestAST.test(input, expect, 307))
	def test_308(self):
		input = '''
			number a[3] <- [1, 2, 3]
			number b[1, 1] <- [[1]]
			string c[1, 2] <- [["aa", "bb"]]
		'''
		expect = '''Program([VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), VarDecl(Id(b), ArrayType([1.0, 1.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0)))), VarDecl(Id(c), ArrayType([1.0, 2.0], StringType), None, ArrayLit(ArrayLit(StringLit(aa), StringLit(bb))))])'''
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
			begin
			end
		'''
		expect = '''Program([Block([])])'''
		self.assertTrue(TestAST.test(input, expect, 311))
	def test_312(self):
		input = '''
			var a <- [1, 1, 1, 1, 1, 2, 4]
			var i <- 0
			for i until len(a) - 1 by 1 begin
				if (i == 1)
					continue
				print(i)
				if (i == 2)
					break
			end  
		'''
		expect = '''Program([VarDecl(Id(a), None, var, ArrayLit(NumLit(1.0), NumLit(1.0), NumLit(1.0), NumLit(1.0), NumLit(1.0), NumLit(2.0), NumLit(4.0))), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(-, CallExpr(Id(len), [Id(a)]), NumLit(1.0)), NumLit(1.0), Block([If((BinaryOp(==, Id(i), NumLit(1.0)), Continue), [], None), CallStmt(Id(print), [Id(i)]), If((BinaryOp(==, Id(i), NumLit(2.0)), Break), [], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 312))
	def test_313(self):
		input = '''
			## This is a comment
			a <- 3
		'''
		expect = '''Program([AssignStmt(Id(a), NumLit(3.0))])'''
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
			return
			break
			continue
		'''
		expect = '''Program([Return(), Break, Continue])'''
		self.assertTrue(TestAST.test(input, expect, 318))
	def test_319(self):
		input = '''
			1
			"1"
			1e-10
			1E10
			[1, 2, 3]
			(1 + 2)
		'''
		expect = '''Program([NumLit(1.0), StringLit(1), NumLit(1e-10), NumLit(10000000000.0), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), BinaryOp(+, NumLit(1.0), NumLit(2.0))])'''
		self.assertTrue(TestAST.test(input, expect, 319))
	def test_320(self):
		input = '''
			a
			a1
			b2
			_a
		'''
		expect = '''Program([Id(a), Id(a1), Id(b2), Id(_a)])'''
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
			a[f()] <- g()
		'''
		expect = '''Program([AssignStmt(ArrayCell(Id(a), [CallExpr(Id(f), [])]), CallExpr(Id(g), []))])'''
		self.assertTrue(TestAST.test(input, expect, 323))
	def test_324(self):
		input = '''
			f()[1, 2] <- [[1, 2]]
		'''
		expect = '''Program([AssignStmt(ArrayCell(CallExpr(Id(f), []), [NumLit(1.0), NumLit(2.0)]), ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))])'''
		self.assertTrue(TestAST.test(input, expect, 324))
	def test_325(self):
		input = '''
			1[2]() <- 2()
		'''
		expect = '''Program([AssignStmt(CallExpr(ArrayCell(NumLit(1.0), [NumLit(2.0)]), []), CallExpr(NumLit(2.0), []))])'''
		self.assertTrue(TestAST.test(input, expect, 325))
	def test_326(self):
		input = '''
			2()()()[1][1] <- 3
		'''
		expect = '''Program([AssignStmt(ArrayCell(ArrayCell(CallExpr(CallExpr(CallExpr(NumLit(2.0), []), []), []), [NumLit(1.0)]), [NumLit(1.0)]), NumLit(3.0))])'''
		self.assertTrue(TestAST.test(input, expect, 326))
	def test_327(self):
		input = '''
			10 * 10 = 1 ... 1
		'''
		expect = '''Program([BinaryOp(..., BinaryOp(=, BinaryOp(*, NumLit(10.0), NumLit(10.0)), NumLit(1.0)), NumLit(1.0))])'''
		self.assertTrue(TestAST.test(input, expect, 327))
	def test_328(self):
		input = '''
			1 + 2 == 2 ... 3 - 3 * 4 = 10() + (3 + 2)
		'''
		expect = '''Program([BinaryOp(..., BinaryOp(==, BinaryOp(+, NumLit(1.0), NumLit(2.0)), NumLit(2.0)), BinaryOp(=, BinaryOp(-, NumLit(3.0), BinaryOp(*, NumLit(3.0), NumLit(4.0))), BinaryOp(+, CallExpr(NumLit(10.0), []), BinaryOp(+, NumLit(3.0), NumLit(2.0)))))])'''
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
		expect = ''''''
		self.assertTrue(TestAST.test(input, expect, 330))
	def test_331(self):
		input = '''
			
		'''
		expect = ''''''
		self.assertTrue(TestAST.test(input, expect, 331))
	def test_340(self):
		input = '''

		'''
		expect = ''''''
		self.assertTrue(TestAST.test(input, expect, 340))
	def test_350(self):
		input = '''

		'''
		expect = ''''''
		self.assertTrue(TestAST.test(input, expect, 350))
	def test_360(self):
		input = '''

		'''
		expect = ''''''
		self.assertTrue(TestAST.test(input, expect, 360))
	def test_370(self):
		input = '''

		'''
		expect = ''''''
		self.assertTrue(TestAST.test(input, expect, 370))
	def test_380(self):
		input = '''

		'''
		expect = ''''''
		self.assertTrue(TestAST.test(input, expect, 380))
	def test_390(self):
		input = '''

		'''
		expect = ''''''
		self.assertTrue(TestAST.test(input, expect, 390))
	def test_400(self):
		input = '''

		'''
		expect = ''''''
		self.assertTrue(TestAST.test(input, expect, 400))