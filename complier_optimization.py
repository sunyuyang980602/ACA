instructions=[]
avail_ops={'add': 'alu', 'mul': 'alu', 'sub': 'alu', 'div': 'alu', 'load': 'ld/st', 'store': 'ld/st', 'stall':'stall', 'bne': 'alu', 'addi': 'alu'}
inn={'add': [2,3], 'mul': [2,3], 'sub': [2,3], 'div': [2,3], 'load': [2], 'store': [1], 'stall':[], 'bne': [1,2], 'addi': [1]}
out={'add': [1], 'mul': [1], 'sub': [1], 'div': [1], 'load': [1], 'store': [2], 'stall':[], 'bne': [3], 'addi': [1]}


import random
random.seed(0)

def add_stall(operations):
    l=len(operations)
    add=[]
    for i in range(l):           
        for jj in range(3):
            j=min(i+jj+1,len(operations)-1)
            if operations[i]=='stall' or operations[j]=='stall':
                continue
            if avail_ops[operations[i][0]]=='alu' and avail_ops[operations[j][0]]=='alu':
                for k in out[operations[i][0]]:
                    for l in inn[operations[j][0]]:
                        if operations[i][k]==operations[j][l]:
                            add.append([i,3])
            elif avail_ops[operations[i][0]]=='alu' and avail_ops[operations[j][0]]=='ld/st':            
                if jj<=2:
                    for k in out[operations[i][0]]:
                        for l in inn[operations[j][0]]:
                            if operations[i][k]==operations[j][l]:
                                add.append([i,2])
            elif avail_ops[operations[i][0]]=='ld/st' and avail_ops[operations[j][0]]=='alu':            
                if jj<=1:
                    for k in out[operations[i][0]]:
                        for l in inn[operations[j][0]]:
                            if operations[i][k]==operations[j][l]:
                                add.append([i,1])
    for i in add:
        while add.count(i) > 1:
            add.remove(i)
    add.sort()
    
    ret=[]
    for i in operations:
        if i=='stall':
            ret.append(i)
        else:
            tmp=''
            for j in i:
                tmp+=j
                tmp+=' '
            ret.append(tmp[:-1])

            
    addret=add[:]
    while len(add)>0:
        for i in range(add[-1][1]):
            ret.insert(add[-1][0]+1,'stall')
        add.pop(-1)
    return ret

if __name__=='__main__':
    #修改了一下，我的这个系统里不支持double类型
    instructions.append('load f0 x0')
    instructions.append('load f1 x1[0]')
    instructions.append('add f2 f1 f0')
    instructions.append('store f2 x1[0]')    
    instructions.append('addi x1 4')
    instructions.append('bne x1 x2 1')
    #修改了一下，我的这个系统里只支持跳转到指定行数(从0算起)

    ops=[]
    for i in instructions:
        op=i.split()
        ops.append(op)

    print('Original operations:')
    for i in ops:
        print(i)
    print('\n')
    ##展开
    unused_register=[i for i in range(32)]
    for i in ops:
        for j in i[1:]:
            if j[0]=='f':
                if unused_register.count(int(j[1:]))==1:
                    unused_register.remove(int(j[1:]))

    replace={}
    ops_final=[]
    prefix=[]
    suffix=[]
    for time in range(3):
        for i in ops:
            if i[0]=='addi' and ops[ops.index(i)+1][0]=='bne':
                #选出中间部分
                start=int(ops[ops.index(i)+1][3])
                end=ops.index(i)
                unroll=ops[start:end]
                prefix=ops[:start]
                suffix=ops[end:]
                if time==0:
                    for j in unroll:
                        ops_final.append(j[:])   
                        
                for j in prefix:
                    for k in j:
                        if k[0]=='f':
                            replace[int(k[1:])]=int(k[1:])
                x=i[1]
                
                for j in unroll:
                    k_new=''
                    for k in j:
                        if x in k:
                            #循环内数组部分平移
                            x_old=int(k[k.index('[')+1:k.index(']')])
                            x_new=x_old+int(i[2])
                            k_new=k[:k.index('[')+1]+str(x_new)+']'
                            ops[ops.index(j)][j.index(k)]=k_new[:]
                    for k in j[1:]:
                        if k[0]=='f':
                            #寄存器重新选择未使用的
                            if int(k[1:]) in replace.keys():
                                r_new=replace[int(k[1:])]
                            else:
                                r_new=unused_register[0]
                                unused_register.pop(0)
                                replace[int(k[1:])]=r_new
                            k_new='f'+str(r_new)
                            ops[ops.index(j)][j.index(k)]=k_new[:]
                break
        for i in ops[start:end]:
            ops_final.append(i[:])                   
                        
                        
    suffix[0][2]=str(int(suffix[0][2])*4)
    ops_final=prefix+ops_final+suffix
                
    
    #方案一：全随机排序，然后加stall--否定，原因：枚举所需次数过多
    #方案二：按优先级分配，优先考虑优先级高的。操作数中，出现次数越高的，优先级越大，alu指令比ld/st优先级高，与之前指令冲突的优先级低

    

####    minlen=4*len(ops)
####    minops=[]
####    for i in  itertools.permutations(ops,len(ops)):
####        ops_with_stall=add_stall(list(i))
####        if len(ops_with_stall)<minlen:
####            minlen=len(ops_with_stall)
####            minops=ops_with_stall
####    print(minlen,minops)



    #方案二
    #详细流程：
    #每次按优先级排序，首先分配最高的，然后在尽可能少加入stall的前提下加入优先级最高的

    

    print('Unrolled operations:')
    for i in ops_final:
        print(i)
    print('\n')

    best_len=9999
    best_ans=[]
    for time in range(1000):
        ans=[]
        not_allocated=ops_final[:]
        not_allocated_backup=not_allocated[:]
        allocated=[]
        loads=[]
        calcs={}
        stores={}
        need_for_addi=[]
        addi=suffix[0]
        load_register=[]
        for i in not_allocated:
            if i[0]=='load':
                loads.append(i)
            for j in i:
                if i[0]=='load' or i[0]=='store':
                    need_for_addi.append(i)

        for i in not_allocated:
            if avail_ops[i[0]]=='alu' and i[0]!='addi' and i[0]!='bne':
                tmp=[]
                for j in inn[i[0]]:
                    for k in loads:
                        if k[1]==i[j]:
                            tmp.append(k)
                            break
                calcs[not_allocated.index(i)]=tmp[:]

                
        for i in not_allocated:
            if i[0]=='store':
                for j in calcs.keys():
                    if i[1] in not_allocated[j]:
                        stores[not_allocated.index(i)]=not_allocated[j]


        for k in range(len(ops_final)):
            to_be_allocated=[]
            for i in not_allocated:
                if i[0]=='load':
                    to_be_allocated.append(i)
                elif i[0]=='store':
                    if stores[not_allocated_backup.index(i)] in allocated:
                        to_be_allocated.append(i)
                elif avail_ops[i[0]]=='alu' and i[0]!='addi' and i[0]!='bne':
                    add_it=True
                    for j in calcs[not_allocated_backup.index(i)]:
                        if j not in allocated:         
                            add_it=False
                    if add_it:
                        to_be_allocated.append(i)
                else:
                    if i[0]=='addi':
                        add_it=True
                        for j in need_for_addi:
                            if j not in allocated:
                                add_it=False
                        if add_it:
                            to_be_allocated.append(i)
                    elif i[0]=='bne':
                        if addi in allocated:
                            to_be_allocated.append(i)
                
            exist_dict={}
            for i in not_allocated:
                for j in i[1:]:
                    try:
                        exist_dict[j]+=1
                    except:
                        exist_dict[j]=1
                    
            priority_dict={}
            for i in to_be_allocated:
                priority_dict[str(i)]=0
                for j in i[1:]:
                    priority_dict[str(i)] += exist_dict[j]

            num_stall={}
            #存字符串
            for i in to_be_allocated:
                tmp=ans+[i]
                num_stall[str(i)]=len(add_stall(tmp))

            least_stall=[]
            #存字符串
            for i in num_stall:
                if num_stall[i]==min(num_stall.values()):
                    least_stall.append(i)

            for i in range(len(least_stall)):
                for j in range(len(least_stall)):
                    if priority_dict[least_stall[i]] > priority_dict[least_stall[j]]:
                        least_stall[i],least_stall[j]=least_stall[j],least_stall[i]

            sum_priority=sum(priority_dict.values())
            choice=random.randint(1,sum_priority)
##            print(choice,priority_dict)
            chosen=least_stall[0]
            for i in list(priority_dict.keys()):
                choice -= priority_dict[i]
                if choice<0:
                    chosen=i
                    break
            for i in not_allocated:
                if str(i)==chosen:                
                    ans.append(i)
                    not_allocated.remove(i)
                    allocated.append(i)
        if len(add_stall(ans))<best_len:
            best_len=len(add_stall(ans))
            best_ans=ans[:]

    print('Rescheduled operations:')
    for i in best_ans:
        print(i)
    print('\n')

    final_ans=add_stall(best_ans)
    print('Final operations:')
    for i in final_ans:
        print(i)
    print('\n')

    
