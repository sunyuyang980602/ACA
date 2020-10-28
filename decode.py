from calc_signed_integar import *
##import calc_signed_integar as si
##import calc_unsigned_integar as ui
zero24=[0]*24
def decode(ins, memory, register, pc):
    op=(ins & 0xff000000)>>24
    op1=(ins & 0xff0000)>>16
    op2=(ins & 0xff00)>>8
    op3=ins & 0xff
    if op==1:
        ##load_byte
        method2=(op2 & 0xe0)>>5
        num2=op2 & 0x1f
        if method2==1:
            tmp=memory[num2]
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
        #load_word
        method2=(op2 & 0xe0)>>5
        num2=op2 & 0x1f
        if method2==2:
            tmp=[memory[num2+i] for i in range(4)
        else:
            print('Error: addressing method not defined.')
            exit(0)
        
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            print('Error: load number to memory')
            exit(0)
        elif method1==2:
            for i in range(4):
                register[num1][8*i:]=tmp[i]
        else:
            print('Error: addressing method not defined.')
            exit(0)
            
    elif op==3:
        ##store_byte
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
            
    elif op==4:
        ##store_word
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
            for i in range(4):
                memory[num2+i]=tmp[8*i:]
        elif method2==2:
            print('Error: store number to register')
            exit(0)
        else:
            print('Error: addressing method not defined.')
            exit(0)
    elif op==5:
        ##storei
        
        num2=op2 & 0xff
        tmp=num2
        
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            l=len(str(bin(tmp))[2:])
            tmpp='0'*(8-l)+str(bin(tmp))[2:]
            for i in range(8):
                register[num2][24+i]=tmpp[i]
        elif method1==2:
            print('Error: store number to register')
            exit(0)
        else:
            print('Error: addressing method not defined.')
            exit(0)
    elif op==6:
        ##move(register to register
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            print('Error: move number from memory')
            exit(0)
        elif method1==2:
            tmp=register[num1]
        else:
            print('Error: addressing method not defined.')
            exit(0)
        
        method2=(op2 & 0xe0)>>5
        num2=op2 & 0x1f
        if method2==1:
            print('Error: move number to memory')
            exit(0)
        elif method2==2:
            register[num2]=tmp
        else:
            print('Error: addressing method not defined.')
            exit(0)
    elif op==7:
        #jump
        num1=op1+op2+op3
        tmp=0
        for i in num1:
            tmp*=2
            tmp+=i
        pc=tmp+0x7f00
        return 'jump'
    elif op==8:
        #beq
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            tmp1=memory[num1]
        elif method1==2:
            tmp1=register[num1]
        else:
            print('Error: addressing method not defined.')
            exit(0)

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

        if EQUAL(tmp1,tmp2):
            tmp=0
            for i in tmp3:
                tmp*=2
                tmp+=i
            pc=tmp+0x7f00
            return 'jump'
    elif op==9:
        #bne
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            tmp1=memory[num1]
        elif method1==2:
            tmp1=register[num1]
        else:
            print('Error: addressing method not defined.')
            exit(0)

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

        if not EQUAL(tmp1,tmp2):
            tmp=0
            for i in tmp3:
                tmp*=2
                tmp+=i
            pc=tmp+0x7f00
            return 'jump'
    elif op==10:
        #bge
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            tmp1=memory[num1]
        elif method1==2:
            tmp1=register[num1]
        else:
            print('Error: addressing method not defined.')
            exit(0)

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

        if GE(tmp1,tmp2):
            tmp=0
            for i in tmp3:
                tmp*=2
                tmp+=i
            pc=tmp+0x7f00
            return 'jump'
    elif op==8:
        #bgt
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            tmp1=memory[num1]
        elif method1==2:
            tmp1=register[num1]
        else:
            print('Error: addressing method not defined.')
            exit(0)

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

        if GT(tmp1,tmp2):
            tmp=0
            for i in tmp3:
                tmp*=2
                tmp+=i
            pc=tmp+0x7f00
            return 'jump'     
        
    elif op==12:
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
        
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            memory[num1]=tmp1
        elif method1==2:
            register[num1]=tmp1
        else:
            print('Error: addressing method not defined.')
            exit(0)

    elif op==13:
        ##addi         
        method2=(op2 & 0xe0)>>5
        num2=op2 & 0x1f
        if method2==1:
            tmp2=memory[num2]
        elif method2==2:
            tmp2=register[num2]
        else:
            print('Error: addressing method not defined.')
            exit(0)
            
        l=len(tmp2)
        num3=[0 for i in range(l)]
        tmp=1
        while tmp<=l:
            num3[l-tmp]=op3%(2**tmp)
            tmp+=1
        

        tmp1=ADD(tmp2,tmp3)
        
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            memory[num1]=tmp1
        elif method1==2:
            register[num1]=tmp1
        else:
            print('Error: addressing method not defined.')
            exit(0)

    elif op==14:
        ##sub           
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

        tmp1=SUB(tmp2,tmp3)
        
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            memory[num1]=tmp1
        elif method1==2:
            register[num1]=tmp1
        else:
            print('Error: addressing method not defined.')
            exit(0)

    elif op==15:
        ##mul         
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

        tmp1=MUL(tmp2,tmp3)
        
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            memory[num1]=tmp1
        elif method1==2:
            register[num1]=tmp1
        else:
            print('Error: addressing method not defined.')
            exit(0)

    elif op==16:
        ##div         
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

        tmp1=DIV(tmp2,tmp3)
        
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            memory[num1]=tmp1
        elif method1==2:
            register[num1]=tmp1
        else:
            print('Error: addressing method not defined.')
            exit(0)

    elif op==17:
        ##xor       
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

        tmp1=XOR(tmp2,tmp3)
        
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            memory[num1]=tmp1
        elif method1==2:
            register[num1]=tmp1
        else:
            print('Error: addressing method not defined.')
            exit(0)
            
    elif op==18:
        ##xori        
        method2=(op2 & 0xe0)>>5
        num2=op2 & 0x1f
        if method2==1:
            tmp2=memory[num2]
        elif method2==2:
            tmp2=register[num2]
        else:
            print('Error: addressing method not defined.')
            exit(0)
            
        l=len(tmp2)
        num3=[0 for i in range(l)]
        tmp=1
        while tmp<=l:
            num3[l-tmp]=op3%(2**tmp)
            tmp+=1
        

        tmp1=XOR(tmp2,tmp3)
        
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            memory[num1]=tmp1
        elif method1==2:
            register[num1]=tmp1
        else:
            print('Error: addressing method not defined.')
            exit(0)
            
    elif op==19:
        ##or       
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

        tmp1=OR(tmp2,tmp3)
        
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            memory[num1]=tmp1
        elif method1==2:
            register[num1]=tmp1
        else:
            print('Error: addressing method not defined.')
            exit(0)  

    elif op==20:
        ##ori        
        method2=(op2 & 0xe0)>>5
        num2=op2 & 0x1f
        if method2==1:
            tmp2=memory[num2]
        elif method2==2:
            tmp2=register[num2]
        else:
            print('Error: addressing method not defined.')
            exit(0)
            
        l=len(tmp2)
        num3=[0 for i in range(l)]
        tmp=1
        while tmp<=l:
            num3[l-tmp]=op3%(2**tmp)
            tmp+=1
        

        tmp1=OR(tmp2,tmp3)
        
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            memory[num1]=tmp1
        elif method1==2:
            register[num1]=tmp1
        else:
            print('Error: addressing method not defined.')
            exit(0)
            
    elif op==21:
        ##and     
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

        tmp1=AND(tmp2,tmp3)
        
        method1=(op1 & 0xe0)>>5
        num1=op1 & 0x1f
        if method1==1:
            memory[num1]=tmp1
        elif method1==2:
            register[num1]=tmp1
        else:
            print('Error: addressing method not defined.')
            exit(0)  

    elif op==22:
        ##andi         
        method2=(op2 & 0xe0)>>5
        num2=op2 & 0x1f
        if method2==1:
            tmp2=memory[num2]
        elif method2==2:
            tmp2=register[num2]
        else:
            print('Error: addressing method not defined.')
            exit(0)
            
        l=len(tmp2)
        num3=[0 for i in range(l)]
        tmp=1
        while tmp<=l:
            num3[l-tmp]=op3%(2**tmp)
            tmp+=1
        

        tmp1=AND(tmp2,tmp3)
        
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
    return 'no_jump'
