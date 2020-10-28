def ADD(x, y):
    l=len(x);
    ans=[0 for i in range(l)]   ##结果
    if x[0] ^ y[0]==1:
        yy=y[:]
        yy[0]=yy[0] ^ 1
        return SUB(x, yy)
    else:
        ans[0]=x[0]
        carry=[0 for i in range(l)] ##进位
        for i in range(l-1):
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

def EQUAL(x, y):
    l=len(x)
    for i in range(l):
        if x[i] ^ y[i]:
            return False
    return True

def AND(x,y):
    tmp=[0 for i in range(len(x))]
    for i in range(len(x)):
        tmp[i]=x[i] & y[i]


def OR(x,y):
    tmp=[0 for i in range(len(x))]
    for i in range(len(x)):
        tmp[i]=x[i] | y[i]


def XOR(x,y):
    tmp=[0 for i in range(len(x))]
    for i in range(len(x)):
        tmp[i]=x[i] ^ y[i]
def GT(x, y):
    #Greater than
    l=len(x)
    if x[0] & ~y[0]:
        return False
    elif ~x[0] & y[0]:
        return True
    elif x[0] & y[0]:
        for i in range(1, l):
            if x[i] & ~y[i]:
                return False
            elif ~x[i] & y[i]:
                return True
            else:
                pass
    else:
        for i in range(1, l):
            if x[i] & ~y[i]:
                return True
            elif ~x[i] & y[i]:
                return False
            else:
                pass
    return False

def GE(x, y):
    l=len(x)
    if x[0] & ~y[0]:
        return False
    elif ~x[0] & y[0]:
        return True
    elif x[0] & y[0]:
        for i in range(1, l):
            if x[i] & ~y[i]:
                return False
            elif ~x[i] & y[i]:
                return True
            else:
                pass
    else:
        for i in range(1, l):
            if x[i] & ~y[i]:
                return True
            elif ~x[i] & y[i]:
                return False
            else:
                pass
    return True

def ST(x, y):
    #smaller than
    return not GE(x, y)

def SE(x, y):
    #smaller than or equal
    return not GT(x, y)
    
    
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
    ans = [0 for i in range(l)]      ##结果
    if x[0] ^ y[0]==1:
        yy=y[:]
        yy[0] = yy[0] ^ 1
        return ADD(x, yy)
    else:
        if GE(x, y):
            if GE(x[1:], y[1:]): 
                borrow = [0 for i in range(l)]   ##借位
                for ii in range(l-1):
                    i = l-ii-1
                    ans[i] = (x[i] ^ y[i]) ^ borrow[i]
                    borrow[i-1] = ((~x[i]) & y[i]) | (~x[i] & borrow[i]) | (y[i] & borrow[i])
            else:
                xx=x[:]
                xx[0]=0
                yy=y[:]
                yy[0]=0
                return SUB(yy,xx)
        else:
            if GE(x[1:], y[1:]):
                xx=x[:]
                xx[0]=0
                yy=y[:]
                yy[0]=0
                anss=SUB(xx,yy)
                anss[0]=1
                return anss
            else:
                xx=x[:]
                xx[0]=0
                yy=y[:]
                yy[0]=0
                anss=SUB(yy,xx)
                anss[0]=1
                return anss
            
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
    


