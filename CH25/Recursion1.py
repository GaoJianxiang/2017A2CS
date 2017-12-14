#kevin Gao S3C2

#recursion 1
def factorial(n):
    if (n==1):
        return 1
    return n*factorial(n-1)

print(factorial(5))

def bunnyEars(n):
    if n ==0:
        return n
    return bunnyEars(n-1)+2

print (bunnyEars(2))

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return n-2+fibonacci(n-3)
print(fibonacci(6))

def bunnyEars2(n):
    if n==0:
        return 0
    if n%2==0:
        return bunnyEars2(n-1)+3
    if n%2==1:
        return bunnyEars2(n-1)+2
print(bunnyEars2(5))

def triangle(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    return n+triangle(n-1)
print(triangle(4))

def sumDigits(n):
    if n <10:
        return n
    else:
        return n%10 + sumDigits(n//10)
print (sumDigits(132))

def count7(n):
    if n == 0:
        return 0
    if n%10 ==7:
        return count7(n//10)+1
    return count7(n//10)
print (count7(277))

def count8(n):
    if n==0:
        return 0
    if n%10 ==8:       
        if (n//10)%10 == 8:
            return count8(n//10)+2
        return count8(n//10)+1
    return count8(n//10)
print(count8(8818))

def powerN(n,m):
    if m == 0:
        return 1
    return n*powerN(n,m-1)
print(powerN(4,3))

def countX(n):
    if len(n)==0:
        return 0
    if n[len(n)-1]=='x':
        return 1 + countX(n[:-1])
    return countX(n[:-1])
print (countX('xxxixixi'))

def countHi(n):
    if len(n)==0 or len(n)==1:
        return 0
    if n[len(n)-1]=='i' and n[len(n)-2]=='H':
        return 1+ countHi(n[:-1])
    return countHi(n[:-1])
print(countHi('HiHiokHi'))

def changeXY(n):
    if len(n)==0:
        return ''
    if n[len(n)-1]=='x':
        return changeXY(n[:-1])+'y'
    return changeXY(n[:-1])+n[len(n)-1]
print(changeXY('xxasdxx'))

def changePi(n):
    if len(n)==2:
        if n[len(n)-1]=='i':
            if n[len(n)-2]=='P':
                return '3.14'
        else:
            return n
    if n[len(n)-1]=='i':
        if n[len(n)-2]=='P':
            return changePi(n[:-2])+'3.14'
    return changePi(n[:-1])+n[len(n)-1]
print (changePi('PiPi'))

def noX(n):
    if len(n)==0:
        return ''
    if n[len(n)-1]=='x':
        return ''+ noX(n[:-1])
    return noX(n[:-1])+n[len(n)-1]
print(noX('xxxssxxdaxx'))

def array6(n,m):
    if len(n)== 0:
        return False
    if n[m]==6:
        return True
    return array6(n,m+1)
print(array6([1,4,1,2,6,7],4))
    
def array11(n,m):
    if m==len(n):
        return 0
    if n[m]==11:
        return 1+ array11(n,m+1)
    return array11(n,m+1)
print (array11([11,2,11],0))

def array220(n,m):
    if m==len(n)+1:
        return False
    if n[m]==n[m+1]/10:
        return True
    return array220(n,m+1)
print(array220([1,2,20],0))

def allstar(n):
    if len(n)==1:
        return n
    return n[0]+'*'+allstar(n[1:])
print(allstar('asdjasldjlashflasfhaf'))
        
def pairstar(n):
    if len(n)==1:
        return n
    if n[0]== n[1]:
        return n[0]+'*'+n[1]+pairstar(n[2:])
    return n[0]+pairstar(n[1:])
print(pairstar('xxyabbc'))

def endX(n):
    if len(n)==1:
        return n
    if n[0]=='x':
        return endX(n[1:])+'x'
    return n[0]+endX(n[1:])
print(endX('xxabasx'))

def countPairs(n):
    if len(n)==2:
        return 0
    if n[0]==n[2]:
        return 1+countPairs(n[1:])
    return 0+countPairs(n[1:])
print(countPairs('xaxabxbx'))

def countAbc(n):
    if len(n)==0:
        return 0
    if n[0:3]=='abc' or n[0:3]=='aba':
        return 1+ countAbc(n[2:])
    return 0 +countAbc(n[1:])
print(countAbc('ababcxxaba'))

def count11(n):
    if len(n)==0:
        return 0
    if n[0:2]=='11' or n[0:3]=='111':
        return 1+count11(n[2:])
    return 0 + count11(n[1:])
print(count11('11absad111a11'))

def stringClean(n):
    if len(n)==0:
        return ''
    if len(n)==1:
        return n
    if n[0]==n[1]:
        return stringClean(n[1:])
    return n[0]+stringClean(n[1:])
print(stringClean('aaabccdd'))

def countHi2(n):
    if len(n)==0:
        return 0
    if n[0:2]=='hi':
        return 1+countHi2(n[2:])
    if n[1:3]=='hi' and n[0]=='x':
        return 0+countHi2(n[3:])
    return 0 + countHi2(n[1:])
print (countHi2('hixhiahi'))

def parenBit(n):
    if len(n)==0:
        return''
    if n[0]!='(':
        return parenBit(n[1:])
    if n[len(n)-1]!=')':
        return parenBit(n[:-1])
print(parenBit('aasda(asdaa)asd'))

def nestParen(n):
    if n=='':
        return True
    if n[0]=='(' and n[-1]==')':
        return nestParen(n[1:-1])
    else:
        return False
print(nestParen('(((x)))'))

def strCount(n, sub):
    if n=='':
        return 0
    if n[0:len(sub)]==sub:
        return 1+strCount(n[len(sub):], sub)
    else:
        return strCount(n[1:], sub)
print(strCount("kevinkevin", 'kevin'))

def strCopies(n, sub, m):

    if n=='' and m==0:
        return True
    if n=='' and m!=0:
        return False
    if n[0:len(sub)]==sub:
        m -= 1
        return strCopies(n[len(sub):], sub, m)
    else:
        return strCopies(n[1:], sub, m)
print(strCopies("kevinkevin", 'kevin', 2))

def strDist(n, sub):
    if len(n)==0:
        return 0
    if n[0:len(sub)]!=sub:
        return strDist(n[1:],sub)
    if n[-len(sub):]!=sub:
        return strDist(n[:-1],sub)
    return len(n)
print(strDist("asdjaslkdaskevinaslkdjal", 'kevin'))

