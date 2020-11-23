import prettytable as pt
#只是为了美化输出
class instruction_status_table():
    def __init__(self,time_spent=None, unit_allocation=None):
        self.instructions=[]
        self.doissue=False
        if time_spent:
            self.time_spent=time_spent
        else:
            self.time_spent={'LD':1, 'MULTD':10, 'SUBD':2, 'ADDD':2, 'DIVD':40}
        if unit_allocation:
            self.unit_allocation=unit_allocation
        else:
            self.unit_allocation={'LD':['Integer'], 'MULTD':['Mult1','Mult2'], 'SUBD':['Add'], 'DIVD':['Divide'], 'ADDD':['Add']}

    def add_instruction(self, instruction0):
        operator0=instruction0.instruction[0]
        instruction0.time_spent=self.time_spent[operator0]
        self.instructions.append(instruction0)
  
    def reset(self):
        for i in self.instructions:
            i.reset()
        self.doissue=False
        
    def process(self, clock, CPU):
        for i in range(len(instructions)):
            if i==0 and not self.instructions[i].issue:
                if self.doissue==False:
                    CPU.todo.append(['issue',self.instructions[i].instruction,self.unit_allocation[self.instructions[i].instruction[0]][0]])
                    self.doissue=True
            else:
                if self.instructions[i-1].issue and not self.instructions[i].issue:
                    for j in self.unit_allocation[self.instructions[i].instruction[0]]:
                        if not CPU.FUST.if_busy(j):
                            if self.doissue==False:
                                CPU.todo.append(['issue',self.instructions[i].instruction,self.unit_allocation[self.instructions[i].instruction[0]][0]])
                                self.doissue=True
            if self.instructions[i].exec_comp and not self.instructions[i].write_result:
                able=True
                for j in CPU.FUST.units:
                    if j.Fj==self.instructions[i].dest or j.Fk==self.instructions[i].dest:
                        if CPU.IST.instructions.index(j.instruction)<i:
                            if not j.instruction.read_oper:
                                able=False
                if able:
                    CPU.todo.append(['write_result',self.instructions[i].instruction])

    def show(self):
        tb=pt.PrettyTable()
        tb.field_names=['instruction','dest','j','k','Issue','Read Oper','Exec Comp','Write Result']
        for i in self.instructions:
            tb.add_row([i.instruction[0],i.instruction[1],i.instruction[2],i.instruction[3],i.issue,i.read_oper,i.exec_comp,i.write_result])
        print(tb)
        return
    

class instruction_in_table():
    def __init__(self, instruction, dest=None, j=None, k=None, issue=None, read_oper=None, exec_comp=None, write_result=None):
        self.instruction=instruction
        self.dest=instruction[1]
        self.j=instruction[2] 
        self.k=instruction[3]
        self.issue=issue
        self.read_oper=read_oper
        self.exec_comp=exec_comp
        self.write_result=write_result
        self.time_spent=None
        self.unit_allocation=None
        ##每周期只能做一件事
        self.dosomething=False

    def do_issue(self, clock, unit, CPU):
        if self.dosomething==False:
            self.dosomething=True
            self.issue=clock
            self.unit_allocation=unit
            CPU.RRST.allocate(self.dest, unit, CPU, self.instruction)
            CPU.FUST.add_ins(self, unit, CPU)

    def do_read_oper(self, clock, CPU):
        if self.dosomething==False:
            self.dosomething=True
            self.read_oper=clock
            for i in CPU.FUST.units:
                if i.name==self.unit_allocation:
                    i.time=CPU.IST.time_spent[self.instruction[0]]

    def do_exec_comp(self, clock):
        if self.dosomething==False:
            self.dosomething=True
            self.exec_comp=clock

    def do_write_result(self, clock, CPU):
        if self.dosomething==False:
            self.dosomething=True
            self.write_result=clock
            CPU.FUST.delete(self.unit_allocation)
            CPU.RRST.unallocate(self.dest)
            self.unit_allocation=None
            ##考虑其他的Rj,Rk
            for j in CPU.FUST.units:
                j.Rj,j.Qj=CPU.RRST.is_ready(j.Fj,self,CPU)
                j.Rk,j.Qk=CPU.RRST.is_ready(j.Fk,self,CPU)
            
    def reset(self):
        self.dosomething=False
                
        
        
class function_unit():
    def __init__(self, name):
        self.time=None
        self.name=name
        self.Busy=False##相当于'no'
        self.Op=None
        self.Fi=None
        self.Fj=None
        self.Fk=None
        self.Qj=None
        self.Qk=None
        self.Rj=None
        self.Rk=None
        self.instruction=None
        
    def reset(self):
        self.time=None
        self.Busy=False##相当于'no'
        self.Op=None
        self.Fi=None
        self.Fj=None
        self.Fk=None
        self.Qj=None
        self.Qk=None
        self.Rj=None
        self.Rk=None
        self.instruction=None

def trans_name(name0):
    trans={'LD':'Load', 'MULTD':'Mult', 'SUBD':'Sub', 'DIVD':'Div', 'ADDD':'Add'}
    return trans[name0]

class functional_unit_status_table():
    def __init__(self, units=None):
        self.units=[]
        if units==None:
            self.units.append(function_unit('Integer'))
            self.units.append(function_unit('Mult1'))
            self.units.append(function_unit('Mult2'))
            self.units.append(function_unit('Add'))
            self.units.append(function_unit('Divide'))
        else:
            for i in units:
                self.units.append(i)

    def if_busy(self, unit_name):
        for i in self.units:
            if i.name==unit_name:
                return i.Busy

    def add_ins(self, ins, unit_name, CPU):
        for i in self.units:
            if i.name==unit_name:
                unit0=i
        unit0.instruction=ins
        unit0.Busy=True
        unit0.Op=trans_name(ins.instruction[0])
        unit0.Fi=ins.instruction[1]
        unit0.Fj=ins.instruction[2]
        unit0.Fk=ins.instruction[3]
        unit0.Rj,unit0.Qj=CPU.RRST.is_ready(unit0.Fj,ins,CPU)
        unit0.Rk,unit0.Qk=CPU.RRST.is_ready(unit0.Fk,ins,CPU)

    def process(self, clock, CPU):
        for i in self.units:
            if i.time:
                i.time-=1
                if i.time==0:
                    CPU.todo.append(['exec_comp',i.instruction.instruction]) 
            if i.Rj and i.Rk and i.instruction:
                if i.instruction.issue and not i.instruction.read_oper:
                    CPU.todo.append(['read_oper',i.instruction.instruction])
        return None
    
    def delete(self, unit_name):
        for i in self.units:
            if i.name==unit_name:
                i.reset()
    
    def show(self):
        print('Functional Unit Status :')
        tb=pt.PrettyTable()
        tb.field_names=['time','name','Busy','Op','Fi','Fj','Fk','Qj','Qk','Rj','Rk']
        for i in self.units:
            tb.add_row([i.time,i.name,i.Busy,i.Op,i.Fi,i.Fj,i.Fk,i.Qj,i.Qk,i.Rj,i.Rk])
        print(tb)
        return
    

class register_result_status_table():
    def __init__(self, instructions):
        self.table2={}
        #table2记录每一条是哪条指令造成的
        self.table={}
        tmp=[]
        for i in instructions:
            for j in i[1:]:
                if j[0]=='F' and j not in tmp:
                    tmp.append(j)
        for i in tmp:
            self.table[i]=None

    def is_ready(self, name, whoask, CPU):
        if self.table.setdefault(name,None):
            for i in range(len(CPU.IST.instructions)):
                if CPU.IST.instructions[i].instruction==self.table2[name]:
                    index_ans=i
            index_ask=CPU.IST.instructions.index(whoask)
            if index_ask<index_ans:
                return [True,None]
            else:
                return [False, self.table[name]]
        else:
            return [True,None]

    def allocate(self, register, unit, CPU, ins):
        self.table[register]=unit
        for i in CPU.FUST.units:
            if i.name==unit:
                self.table2[register]=ins

    def unallocate(self, register):
        self.table[register]=None
        self.table2[register]=None

    def show(self):
        tb=pt.PrettyTable()
        tmp=['Register Result Status']
        val=['Functional Unit']
        for i in self.table.keys():
            if i:
                if i[0]=='F':
                    tmp.append(i)
                    val.append(self.table[i])
        tb.field_names=(tmp)
        tb.add_row(val)
        print(tb)
        return
    

class central_processing_unit():
    def __init__(self, IST, FUST, RRST):
        self.todo=list()
        self.IST=IST
        self.FUST=FUST
        self.RRST=RRST
        self.clock=0

    def is_over(self):
        for i in self.IST.instructions:
            if not i.write_result:
                return False
        return True
    
    def process(self):
        self.clock+=1
        self.reset()
        self.IST.reset()
        self.FUST.process(self.clock,self)
        self.IST.process(self.clock,self)
        for i in self.todo:
            if i[0]=='exec_comp':
                for j in self.IST.instructions:
                    if j.instruction==i[1]:
                        j.do_exec_comp(self.clock)
            elif i[0]=='read_oper':
                for j in self.IST.instructions:
                    if j.instruction==i[1]:
                        j.do_read_oper(self.clock,self)
            elif i[0]=='issue':
                for j in self.IST.instructions:
                    if j.instruction==i[1]:
                        j.do_issue(self.clock,i[2],self)
            elif i[0]=='write_result':
                for j in self.IST.instructions:
                    if j.instruction==i[1]:
                        j.do_write_result(self.clock,self)
                
    def reset(self):
        self.todo=list()

    def show(self):
        print('Clock:',self.clock)
        self.IST.show()
        self.FUST.show()
        self.RRST.show()
    
    def execute(self):
        ##version1
        while not self.is_over():
            self.process()
            self.show()
            a=input()
            if a:
                try:
                    aa=int(a)
                    if aa==-1:
                        while not self.is_over():
                            print('\n')
                            self.process()
                            self.show()
                        return
                    while aa>self.clock+1:
                        print('\n')
                        self.process()
                        self.show()
                except:
                    break
        ##version2
        # while True:
        #     a=int(input())
        #     if a==0:
        #         self.process()
        #         self.show()
        #     elif a>self.clock:
        #         while a>self.clock:
        #             self.process()
        #             self.show()
        #     elif a==-1:
        #         while not self.is_over():
        #             self.process()
        #             self.show()


if __name__=='__main__':
    ist=instruction_status_table()
    fust=functional_unit_status_table()
    instructions=[]
    instructions.append('LD F6 34+ R2'.split())
    instructions.append('LD F2 45+ R3'.split())
    instructions.append('MULTD F0 F2 F4'.split())
    instructions.append('SUBD F8 F6 F2'.split())
    instructions.append('DIVD F10 F0 F6'.split())
    instructions.append('ADDD F6 F8 F2'.split())
    for i in instructions:
        tmp=instruction_in_table(i)
        ist.add_instruction(tmp)
    rrst=register_result_status_table(instructions)
    cpu=central_processing_unit(ist,fust,rrst)
    cpu.execute()
