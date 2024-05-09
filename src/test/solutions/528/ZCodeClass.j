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
	goto Label6
Label4:
	ldc 1.0
	fload_1
	fadd
	fstore_1
Label6:
	fload_1
	ldc 3.0
	fcmpl
	ifne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifne Label5
Label9:
.var 2 is y F from Label9 to Label10
	ldc 0.0
	fstore_2
	goto Label13
Label11:
	ldc 1.0
	fload_2
	fadd
	fstore_2
Label13:
	fload_2
	ldc 1.0
	fcmpl
	ifne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifne Label12
Label16:
.var 3 is z F from Label16 to Label17
	ldc 0.0
	fstore_3
	goto Label20
Label18:
	ldc 1.0
	fload_3
	fadd
	fstore_3
Label20:
	fload_3
	ldc 1.0
	fcmpl
	ifne Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	ifne Label19
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
	goto Label18
Label19:
Label17:
	goto Label11
Label12:
Label10:
	goto Label4
Label5:
Label3:
Label1:
	return
.limit stack 14
.limit locals 4
.end method
