def assemble(ins_asm):
#汇编，将汇编语言翻译成机器语言
    operation=ins_asm.split()
    op=operation[0]
    ins=0
    if op=='Load':
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
            #load byte
            ins+=0x1000000
            ins+=0x4000
        elif op2[0]=='#':
            #load word
            ins+=0x2000000
            ins+=0x2000
        ins +=num2<<8
    elif op=='Store':
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            #store word
            ins+=0x4000000
            ins+=0x400000
        elif op1[0]=='#':
            #store byte
            ins+=0x3000000
            ins+=0x200000
        ins +=num1<<16
        
        op2=operation[2]
        num2=int(op2[1:])
        if op2[0]=='r':
            ins+=0x4000
        elif op2[0]=='#':
            ins+=0x2000
        ins += num2<<8
    elif op=='Storei':
        ins+=0x5000000
        op1=operation[1]
        num1=int(op1[:])
        ins +=num1<<16
        
        op2=operation[2]
        num2=int(op2[1:])
        if op2[0]=='r':
            ins+=0x4000
        elif op2[0]=='#':
            ins+=0x2000
        ins += num2<<8
    elif op=='Move':
        ins+=0x6000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
        op2=operation[2]
        num2=int(op2[1:])
        if op2[0]=='r':
            ins+=0x4000
        elif op2[0]=='#':
            ins+=0x2000
        ins +=num2<<8
    elif op=='Jump':
        ins+=0x7000000
        op1=operation[1]
        num1=int(op1[1:])
        ins += num1<<16
    elif op=='Beq':
        ins+=0x8000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
        op2=operation[2]
        num2=int(op2[1:])
        if op2[0]=='r':
            ins+=0x4000
        elif op2[0]=='#':
            ins+=0x2000
        ins +=num2<<8
        
        op3=operation[3]
        num3=int(op3[1:])
        ins +=num3     
    elif op=='Bne':
        ins+=0x9000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
        op2=operation[2]
        num2=int(op2[1:])
        if op2[0]=='r':
            ins+=0x4000
        elif op2[0]=='#':
            ins+=0x2000
        ins +=num2<<8
        
        op3=operation[3]
        num3=int(op3[1:])
        ins +=num3     
    elif op=='Bge':
        ins+=0xa000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
        op2=operation[2]
        num2=int(op2[1:])
        if op2[0]=='r':
            ins+=0x4000
        elif op2[0]=='#':
            ins+=0x2000
        ins +=num2<<8
        
        op3=operation[3]
        num3=int(op3[1:])
        ins +=num3     
    elif op=='Bgt':
        ins+=0xb000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
        op2=operation[2]
        num2=int(op2[1:])
        if op2[0]=='r':
            ins+=0x4000
        elif op2[0]=='#':
            ins+=0x2000
        ins +=num2<<8
        
        op3=operation[3]
        num3=int(op3[1:])
        ins +=num3        
    elif op=='Add':
        ins+=0xc000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
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
    elif op=='Addi':
        ins+=0xd000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
        op2=operation[2]
        num2=int(op2[1:])
        if op2[0]=='r':
            ins+=0x4000
        elif op2[0]=='#':
            ins+=0x2000
        ins +=num2<<8
        
        op3=operation[3]
        num3=int(op3[1:])
        ins +=num3        
    elif op=='sub':
        ins+=0xe000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
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
    elif op=='mul':
        ins+=0xf000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
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
    elif op=='div':
        ins+=0x10000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
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
    elif op=='xor':
        ins+=0x11000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
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
    elif op=='xori':
        ins+=0x12000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
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
    elif op=='or':
        ins+=0x13000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
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
    elif op=='ori':
        ins+=0x14000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
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
    elif op=='and':
        ins+=0x15000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
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
    elif op=='andi':
        ins+=0x16000000
        op1=operation[1]
        num1=int(op1[1:])
        if op1[0]=='r':
            ins+=0x400000
        elif op1[0]=='#':
            ins+=0x200000
        ins += num1<<16
        
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
##    print(ins)
##    print(hex(ins))
    return ins
