.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static numArr [[[F

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public static readNumber()F
Label0:
.var 0 is arg F from Label0 to Label1
	new java/util/Scanner
	dup
	dup
	getstatic java/lang/System/in Ljava/io/InputStream;
	invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
	invokevirtual java/util/Scanner.nextFloat()F
	fstore_0
	invokevirtual java/util/Scanner/nextLine()Ljava/lang/String;
	pop
	fload_0
	freturn
Label1:
.limit stack 4
.limit locals 1
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

.method public static readString()Ljava/lang/String;
Label0:
	new java/util/Scanner
	dup
	getstatic java/lang/System/in Ljava/io/InputStream;
	invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
	invokevirtual java/util/Scanner.nextLine()Ljava/lang/String;
	areturn
Label1:
.limit stack 3
.limit locals 0
.end method

.method public static writeString(Ljava/lang/String;)V
Label0:
.var 0 is arg Ljava/lang/String; from Label0 to Label1
	getstatic java/lang/System/out Ljava/io/PrintStream;
	aload_0
	invokevirtual java/io/PrintStream.print(Ljava/lang/String;)V
	return
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static readBool()Z
Label0:
.var 0 is arg Z from Label0 to Label1
	new java/util/Scanner
	dup
	dup
	getstatic java/lang/System/in Ljava/io/InputStream;
	invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
	invokevirtual java/util/Scanner.nextBoolean()Z
	istore_0
	invokevirtual java/util/Scanner/nextLine()Ljava/lang/String;
	pop
	iload_0
	ireturn
Label1:
.limit stack 4
.limit locals 1
.end method

.method public static writeBool(Z)V
Label0:
.var 0 is arg Z from Label0 to Label1
	getstatic java/lang/System/out Ljava/io/PrintStream;
	iload_0
	invokevirtual java/io/PrintStream.print(Z)V
	return
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static getArr()[[[F
Label0:
	iconst_3
	anewarray [[F
	dup
	iconst_0
	iconst_1
	anewarray [F
	dup
	iconst_0
	iconst_1
	newarray float
	dup
	iconst_0
	ldc 0.0
	fastore
	aastore
	aastore
	dup
	iconst_1
	iconst_1
	anewarray [F
	dup
	iconst_0
	iconst_1
	newarray float
	dup
	iconst_0
	ldc 1.0
	fastore
	aastore
	aastore
	dup
	iconst_2
	iconst_1
	anewarray [F
	dup
	iconst_0
	iconst_1
	newarray float
	dup
	iconst_0
	ldc 2.0
	fastore
	aastore
	aastore
	areturn
Label1:
	return
.limit stack 10
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	invokestatic ZCodeClass/getArr()[[[F
	putstatic ZCodeClass/numArr [[[F
.var 1 is x F from Label2 to Label3
	ldc 0.0
	fstore_1
Label4:
	fload_1
	ldc 3.0
	fcmpl
	ifne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifne Label5
Label8:
.var 2 is y F from Label8 to Label9
	ldc 0.0
	fstore_2
Label10:
	fload_2
	ldc 1.0
	fcmpl
	ifne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifne Label11
Label14:
.var 3 is z F from Label14 to Label15
	ldc 0.0
	fstore_3
Label16:
	fload_3
	ldc 1.0
	fcmpl
	ifne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifne Label17
	getstatic ZCodeClass/numArr [[[F
	fload_1
	f2i
	aaload
	fload_2
	f2i
	aaload
	fload_3
	f2i
	faload
	invokestatic ZCodeClass/writeNumber(F)V
	ldc 1.0
	fload_3
	fadd
	fstore_3
	goto Label16
Label17:
Label15:
	ldc 1.0
	fload_2
	fadd
	fstore_2
	goto Label10
Label11:
Label9:
	ldc 1.0
	fload_1
	fadd
	fstore_1
	goto Label4
Label5:
Label3:
Label1:
	return
.limit stack 14
.limit locals 4
.end method
