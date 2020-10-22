def ADD(x, y):
    l=len(x);
    ans=[0 for i in range(l)]   ##结果
    carry=[0 for i in range(l)] ##进位
    for i in range(l):
        j=l-1-i
        ans[j] = (x[j] ^ y[j]) ^ carry[j]
        carry[j-1] = (x[j] & y[j]) | (x[j] & carry[j]) | (y[j] & carry[j])
    return ans
        
def MUL(x, y):
    l=len(x)
    ans=[0 for i in range(2*l)]
    for ii in range(l):
        i=l-1-ii
        for jj in range(l):
            j=l-1-jj
            tmp = (x[i] & y[j])
            for k in range(i+j+1):
                tmpp=ans[i+j+1] & tmp
                for ll in range(i+j+1, k, -1):
                    tmpp = ans[ll] & tmpp
                ans[k] = ans[k] ^ tmpp
            ans[i+j+1] = ans[i+j+1] ^ (x[i] & y[j])
    return ans[l:]

def GT(x, y):
    #Greater than
    l=len(x)
    for i in range(l):
        if x[i] & ~y[i]:
            return True
        elif ~x[i] & y[i]:
            return False
        else:
            pass
    return False

def GE(x, y):
    #Greater than or Equal
    l=len(x)
    for i in range(l):
        if x[i] & ~y[i]:
            return True
        elif ~x[i] & y[i]:
            return False
        else:
            pass
    return True
    
    
def NEXT(x):
    tmp = [0 for i in x]
    tmp[-1] = 1
    return ADD(x, tmp)

def LAST(x):
    tmp = [0 for i in x]
    tmp[-1] = 1
    return SUB(x, tmp)

def DIV(x, y):
    tmp = [0 for i in x]
    while True:
        tmp = NEXT(tmp)
        if GT(MUL(y, tmp), x):
            return [LAST(tmp), SUB(x, MUL(y, LAST(tmp)))]
        


def SUB(x, y):
    l=len(x)
    if not GE(x,y):
        print('Sub Error: negative result. Returning zero.')
        return [0 for i in range(l)]
    else:
        pass
    ans = [0 for i in range(l)]      ##结果
    borrow = [0 for i in range(l)]   ##借位
    for ii in range(l):
        i = l-ii-1
        ans[i] = (x[i] ^ y[i]) ^ borrow[i]
        borrow[i-1] = ((~x[i]) & y[i]) | (~x[i] & borrow[i]) | (y[i] & borrow[i])
    return ans
        

if __name__=='__main__':
    a=[0,0,0,0,0,0,0,1]
    b=[0,0,0,0,0,0,1,1]
    c=[0,0,0,0,0,1,1,1]
    d=[0,0,0,0,0,1,0,0]

    print(a,'+',b,'=',ADD(a,b))
    print(b,'+',b,'=',ADD(b,b))

    
    print(a,'*',b,'=',MUL(a,b))
    
    print(b,'*',b,'=',MUL(b,b))
    
    print(c,'*',c,'=',MUL(c,c))


    print(a,'-',b,'=',SUB(a,b))
    print(b,'-',a,'=',SUB(b,a))
    print(d,'-',b,'=',SUB(d,b))

    print(d,'-',a,'=',SUB(d,a))

    print(d,'/',a,'=',DIV(d,a)[0], 'remains', DIV(d,a)[1])
    print(d,'/',b,'=',DIV(d,b)[0], 'remains', DIV(d,b)[1])
    print(d,'/',c,'=',DIV(d,c)[0], 'remains', DIV(d,c)[1])
    


