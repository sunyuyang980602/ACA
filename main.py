'''
32位指令
8位操作，三个八位的地址
地址中前三位表示寻址方式，后五位表示数
1：立即
2：寄存器
3：直接（内存地址记在寄存器中）

八位操作：
1：load
2：store
3：add
在python3.7.6，于2020/10/16/21:58成功运行
'''

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
# 内存地址0x7f00~0x8000存放指令
#注：实际上为0x7f000000~0x80000000,24位空间，为了jump指令

if __name__=='__main__':
    instructions.append('Load r1 #0')#自动判断load_byte与load_word
    instructions.append('Load r2 #1')
    instructions.append('Add r3 r1 r2')
    instructions.append('Store r3 #3')
    memory[0]=[0 for i in range(8)]
    memory[1]=[0 for i in range(8)]
    memory[0][7]=1#0号单元置1
    memory[1][6]=1#1号单元置2
    #1+2=3

    print('开始编译')
    address=0x7f00
    for i in instructions:
        ins=assemble(i)
        l=len(str(bin(ins))[2:])
        tmp='0'*(32-l)+str(bin(ins))[2:]
        #前缀用0补齐32位
        for j in range(4):
            for k in range(8):
                memory[address+j][k]=int(tmp[8*j+k])
        address+=4

    print('编译结束，开始译码执行')
    pc=0x7f00
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
        if decode(ins, memory, register, pc)=='jump':
            pass
        else:
            pc+=4
        print('memory:\n',memory[0],'\n',memory[1],'\n',memory[2],'\n',memory[3])
        print('register:\n',register[0],'\n',register[1],'\n',register[2],'\n',register[3])
        print('\n')
    print(memory[3])
