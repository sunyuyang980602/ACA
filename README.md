# ACA\n
Advanced Computer Architecture Homework\n
Coded by Sunyuyang, 2020/10\n
设计并通过python实现指令集\n
memory地址空间大小32位，每单元八位\n
有32个32位寄存器\n
指令集目前包含load_byte, load_word, store_byte, store_word, storei, move, jump, beq, bne, bge, blt, add, addi, sub, mul, div, xor, xori, or, ori, and, andi指令\n
指令长度32位，八位操作，然后接三个八位的操作数。\n
操作数包含3位取址方式和5位数字。\n
汇编指令格式如\n
load_byte r1 #1\n
add r3 r1 r2\n
store_byte r3 #3\n
