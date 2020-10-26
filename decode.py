from calc_unsigned_integar import *
zero24=[0]*24
def decode(ins, memory, register):
    op=(ins & 0xff000000)>>24
    op1=(ins & 0xff0000)>>16
    op2=(ins & 0xff00)>>8
    op3=ins & 0xff
    if op==1:
        ##load
        method2=(op2 & 0xe0)>>5
        num2=op2 & 0x1f
        if method2==1:
            tmp=memory[num2]
        elif method2==2:
            print('Error: load number from register')
            exit(0)
        else:
            print('Error: addressing method not defined.')
            exit(0)
        
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            print('Error: load number to memory')
            exit(0)
        elif method1==2:
            register[num1]=zero24+tmp
        else:
            print('Error: addressing method not defined.')
            exit(0)

            
    elif op==2:
        ##store
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            print('Error: store number from memory')
            exit(0)
        elif method1==2:
            tmp=register[num1]
        else:
            print('Error: addressing method not defined.')
            exit(0)
        
        method2=(op2 & 0xe0)>>5
        num2=op2 & 0x1f
        if method2==1:
            memory[num2]=tmp[24:]
        elif method2==2:
            print('Error: store number to register')
            exit(0)
        else:
            print('Error: addressing method not defined.')
            exit(0)

    elif op==3:
        ##add            
        method2=(op2 & 0xe0)>>5
        num2=op2 & 0x1f
        if method2==1:
            tmp2=memory[num2]
        elif method2==2:
            tmp2=register[num2]
        else:
            print('Error: addressing method not defined.')
            exit(0)
            
        method3=(op3 & 0xe0)>>5
        num3=op3 & 0x1f
        if method3==1:
            tmp3=memory[num3]
        elif method3==2:
            tmp3=register[num3]
        else:
            print('Error: addressing method not defined.')
            exit(0)

        tmp1=ADD(tmp2,tmp3)
##        tmp1=tmp2+tmp3
        
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            memory[num1]=tmp1
        elif method1==2:
            register[num1]=tmp1
        else:
            print('Error: addressing method not defined.')
            exit(0)

    else:
        print('Operation not defined')
        exit(0)
