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
memory=[[] for i in range(0x8000)]
for i in range(0x8000):
    for j in range(8):
        memory[i].append(0)
        
memory=[0]*0x80000000
register=[0]*0x20


pc=[] 


if __name__=='__main__':
    pc.append('Load r1 #0')
    pc.append('Load r2 #1')
    pc.append('Add r3 r1 r2')
    pc.append('Store r3 #3')
    memory[0]=1
    memory[1]=2
    
    for i in pc:
        ins=assemble(i)
        decode(ins)
        print(i)
        print('memory:\t\t',memory[0],memory[1],memory[2],memory[3])
        print('register:\t',register[0],register[1],register[2],register[3])
        print('\n')
    print(memory[3])
