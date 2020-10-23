def assemble(ins_asm):
#汇编，将汇编语言翻译成机器语言
    operation=ins_asm.split()
    op=operation[0]
    ins=0
    if op=='Load':
        ins+=0x1000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins +=num1<<16
        
        op2=operation[2]
        num2=int(op2[1:])
        if op2[0]=='r':
            ins+=0x4000
        elif op2[0]=='#':
            ins+=0x2000
        ins +=num2<<8
    elif op=='Store':
        ins+=0x2000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins +=num1<<16
        
        op2=operation[2]
        num2=int(op2[1:])
        if op2[0]=='r':
            ins+=0x4000
        elif op2[0]=='#':
            ins+=0x2000
        ins +=num2<<8
    elif op=='Add':
        ins+=0x3000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins +=num1<<16
        
        op2=operation[2]
        num2=int(op2[1:])
        if op2[0]=='r':
            ins+=0x4000
        elif op2[0]=='#':
            ins+=0x2000
        ins +=num2<<8
        
        op3=operation[3]
        num3=int(op3[1:])
        if op3[0]=='r':
            ins+=0x40
        elif op3[0]=='#':
            ins+=0x20
        ins +=num3
    print(hex(ins))
    return ins
