# ACA  
Advanced Computer Architecture Homework  
Coded by Sunyuyang, 2020/10  
设计并通过python实现指令集  
memory地址空间大小32位，每单元八位  
前面存放数据，0x7f000000-0x80000000存放指令（保留24位以方便jump指令跳转）  
有32个32位寄存器  
指令集目前包含load_byte, load_word, store_byte, store_word, storei, move, jump, beq, bne, bge, blt, add, addi, sub, mul, div, xor, xori, or, ori, and, andi指令  
load与store根据寻址方法自动判别  
指令长度32位，八位操作，然后接三个八位的操作数。  
操作数包含3位取址方式和5位数字。  
汇编指令格式如  
load r1 #1  
add r3 r1 r2  
store_byte r3 #3  

目前存在的问题：  
固定长度指令，因此branch操作只能跳转八位
