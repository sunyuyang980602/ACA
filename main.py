from assemble import *
from decode import *
memory=[[] for i in range(0x8000)]
for i in range(0x8000):
    for j in range(8):
        memory[i].append(0)


register=[[] for i in range(32)]
for i in range(32):
    for j in range(32):
        register[i].append(0)
        


pc=0
instructions=[]
#这个数组临时存放汇编指令
# 内存地址0x7000~0x8000存放指令

if __name__=='__main__':
    instructions.append('Load r1 #0')
    instructions.append('Load r2 #1')
    instructions.append('Add r3 r1 r2')
    instructions.append('Store r3 #3')
    memory[0]=[0 for i in range(8)]
    memory[1]=[0 for i in range(8)]
    memory[0][7]=1
    memory[1][6]=1

    print('开始编译')
    address=0x7000
    for i in instructions:
        ins=assemble(i)
        l=len(str(bin(ins))[2:])
        tmp='0'*(32-l)+str(bin(ins))[2:]        
        for j in range(4):
            for k in range(8):
                memory[address+j][k]=int(tmp[8*j+k])
        address+=4

    print('编译结束，开始译码执行')
    pc=0x7000
    while True:
        ins=0
        for i in range(pc,pc+4):
            for j in range(8):
                ins*=2
                ins+=memory[i][j]
        print('指令为：',hex(ins))
        if ins==0:
            #0指令为终止指令
            break
        decode(ins, memory, register)
        pc+=4
        print('memory:\n',memory[0],'\n',memory[1],'\n',memory[2],'\n',memory[3])
        print('register:\n',register[0],'\n',register[1],'\n',register[2],'\n',register[3])
        print('\n')
    print(memory[3])
