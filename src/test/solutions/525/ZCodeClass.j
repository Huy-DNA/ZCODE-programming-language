.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static strArr [Ljava/lang/String;

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

.method public static getArr()[Ljava/lang/String;
Label0:
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "an"
	aastore
	dup
	iconst_1
	ldc "huy"
	aastore
	areturn
Label1:
	return
.limit stack 4
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	invokestatic ZCodeClass/getArr()[Ljava/lang/String;
	putstatic ZCodeClass/strArr [Ljava/lang/String;
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
	fstore_2
	fload_1
	ldc 2.0
	fcmpl
	ifne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifne Label5
	getstatic ZCodeClass/strArr [Ljava/lang/String;
	fload_1
	f2i
	aaload
	invokestatic ZCodeClass/writeString(Ljava/lang/String;)V
	fload_2
	fstore_1
	goto Label4
Label5:
	fload_2
	fstore_1
Label3:
Label1:
	return
.limit stack 6
.limit locals 3
.end method
