.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object

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

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	ldc 1.0
	ldc 1.0
	fadd
	ldc 2.0
	fcmpl
	ifeq Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label7
	ldc "1 + 1 != 2"
	invokestatic ZCodeClass/writeString(Ljava/lang/String;)V
	goto Label6
Label7:
	ldc 2.0
	ldc 2.0
	fadd
	ldc 3.0
	fcmpl
	ifne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	ldc "2 + 2 = 3"
	invokestatic ZCodeClass/writeString(Ljava/lang/String;)V
	goto Label6
Label10:
	ldc 1.0
	ldc 3.0
	fadd
	ldc 4.0
	fcmpl
	ifeq Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label13
	ldc "1 + 3 != 4"
	invokestatic ZCodeClass/writeString(Ljava/lang/String;)V
	goto Label6
Label13:
	ldc 1.0
	ldc 3.0
	fadd
	ldc 4.0
	fcmpl
	ifne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ldc 1.0
	ldc 1.0
	fadd
	ldc 3.0
	fcmpl
	ifne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	iand
	ifle Label18
	ldc "1 + 3 = 4 and 1 +1 = 3"
	invokestatic ZCodeClass/writeString(Ljava/lang/String;)V
	goto Label6
Label18:
	ldc "???"
	invokestatic ZCodeClass/writeString(Ljava/lang/String;)V
Label6:
Label3:
Label1:
	return
.limit stack 22
.limit locals 1
.end method
