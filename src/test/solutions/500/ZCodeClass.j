.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object

.method public static readNumber()F
Label0:
	new java/util/Scanner
	dup
	getstatic java/lang/System/in Ljava/io/InputStream;
	invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
	invokevirtual java/util/Scanner.nextFloat()F
	freturn
Label1:
.limit stack 3
.limit locals 0
.end method

.method public static writeNumber(F)V
Label0:
.var 0 is arg F from Label0 to Label1
	getstatic java/lang/System/out Ljava/io/PrintStream;
	fload_0
	invokevirtual java/io/PrintStream.print(F)V
	return
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is main [Ljava/lang/String; from Label0 to Label1
Label2:
	ldc 1.0
	invokestatic ZCodeClass/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
